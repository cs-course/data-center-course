# -*- coding: utf-8 -*-
"""课程配图重绘工具：由一份几何描述同时产出 .drawio 可编辑原稿与 .svg 成品。

用法（每张图一个一次性脚本，运行后即可删除脚本，产物只需保留两个文件）：

    from redraw_kit import Diagram, CELL, PBOX, BLUE, RED
    d = Diagram(268, 444, "c-pointer-xxx", "标题", "无障碍描述")
    d.heading(134, 18, "① 两个指针指向同一数组")
    d.memory(104, 36, 60, 28, ["", "", "⋮", ""])
    d.pointer(16, 36, "pa1").to(102, 50)
    d.caption(12, 158, 244, "pa2 − pa1 = 9 − 0 = 9  （下标之差）")
    d.save()

约定（与 c-pointer-sub.svg 试点一致）：
  * images/<name>.drawio —— 纯 mxGraphModel XML，可用 draw.io 直接打开修改
  * images/<name>.svg    —— 纯 <rect>/<path>/<text>，不依赖 foreignObject；
    content 属性内嵌压缩后的 drawio 原稿，用 draw.io 打开 SVG 也能继续编辑
  * 配色：灰内存格 / 淡蓝指针框 / 深红箭头 / 浅蓝结论条
"""
import base64
import urllib.parse
import zlib
from lxml import etree

INK = "#1A1A1A"
BLUE = "#1F3864"
CELL = "#CCCCCC"          # 内存格
PBOX_FILL = "#DAE8FC"     # 指针变量框填充
PBOX_LINE = "#6C8EBF"     # 指针变量框描边
PBOX = (PBOX_FILL, PBOX_LINE)
RED = "#C0392B"           # 指向箭头
CAP_BG = "#F2F6FC"        # 结论条底色
CAP_LINE = "#D6E4F0"
SENTINEL = "#FFFF99"      # 需要强调的格子（如 \0）
FONT = "Helvetica, Arial, 'Microsoft YaHei', sans-serif"
SVG_NS = "http://www.w3.org/2000/svg"

_STYLE_VERTEX = "rounded=0;whiteSpace=wrap;html=1;"
_STYLE_TEXT = ("text;html=1;strokeColor=none;fillColor=none;"
               "align=%s;verticalAlign=middle;whiteSpace=wrap;rounded=0;"
               "fontSize=%d;%sfontColor=%s;")


class Diagram:
    def __init__(self, width, height, name, title="", desc=""):
        self.W, self.H, self.name = width, height, name
        self.title, self.desc = title or name, desc or name
        self.els = []

    # ---------- 基础图元 ----------
    def rect(self, x, y, w, h, value="", fill=CELL, stroke="#000000", size=15,
             color=INK, bold=False, rx=0, font=FONT):
        self.els.append(dict(kind="rect", x=x, y=y, w=w, h=h, value=value,
                             fill=fill, stroke=stroke, size=size, color=color,
                             bold=bold, rx=rx, font=font))
        return self

    def text(self, x, y, value, size=14, color=INK, bold=False,
             anchor="middle", width=240, font=FONT):
        self.els.append(dict(kind="text", x=x, y=y, value=value, size=size,
                             color=color, bold=bold, anchor=anchor, w=width,
                             font=font))
        return self

    def arrow(self, x1, y1, x2, y2, color=RED, label="", label_dy=-10):
        self.els.append(dict(kind="arrow", x1=x1, y1=y1, x2=x2, y2=y2,
                             color=color))
        if label:
            self.text((x1 + x2) / 2, (y1 + y2) / 2 + label_dy, label,
                      size=12, color=color, bold=True, width=90)
        return self

    def path(self, d, color=RED, arrow=True, width=1.8):
        """自定义路径；arrow=True 时在末端加箭头。d 用 SVG path 语法。"""
        self.els.append(dict(kind="path", d=d, color=color, arrow=arrow,
                             width=width))
        return self

    def line(self, x1, y1, x2, y2, color="#BBBBBB", dash=True):
        self.els.append(dict(kind="line", x1=x1, y1=y1, x2=x2, y2=y2,
                             color=color, dash=dash))
        return self

    # ---------- 组合图元 ----------
    def heading(self, x, y, value, width=244):
        return self.text(x, y, value, size=13, bold=True,
                         color="#333333", width=width)

    def divider(self, x1, y1, x2, y2):
        return self.line(x1, y1, x2, y2)

    def caption(self, x, y, w, value, size=13, h=26):
        self.rect(x, y, w, h, fill=CAP_BG, stroke=CAP_LINE, rx=4)
        return self.text(x + w / 2, y + h / 2, value, size=size,
                         color=BLUE, bold=True, width=w - 8)

    def memory(self, x, y, w, h, cells, size=15, fills=None):
        """一列内存格。cells 为每格文字列表；fills 可逐格指定颜色。"""
        for i, v in enumerate(cells):
            f = fills[i] if fills else CELL
            self.rect(x, y + i * h, w, h, v, fill=f, size=size,
                      bold=(v == r"\0"))
        return self

    def grid(self, x, y, cw, ch, values, fills=None, size=14):
        """二维方格。values 为二维列表（行 -> 列）。"""
        for r, row in enumerate(values):
            for c, v in enumerate(row):
                f = fills[r][c] if fills else CELL
                self.rect(x + c * cw, y + r * ch, cw, ch, v, fill=f, size=size)
        return self

    def pointer(self, x, y, label, w=56, h=28):
        """指针变量框，返回带 .to() 的小对象。"""
        self.rect(x, y, w, h, label, fill=PBOX_FILL, stroke=PBOX_LINE,
                  size=15, color=BLUE, bold=True)
        return _Ptr(self, x, y, w, h)

    # ---------- 输出 ----------
    def _drawio_style(self, e):
        if e["kind"] == "rect":
            s = _STYLE_VERTEX + "fillColor=%s;strokeColor=%s;" % (
                e["fill"], e["stroke"])
            if e["rx"]:
                s += "rounded=1;arcSize=12;"
            s += "fontSize=%d;%sfontColor=%s;align=center;verticalAlign=middle;" % (
                e["size"], "fontStyle=1;" if e["bold"] else "", e["color"])
            return s
        return _STYLE_TEXT % ("center" if e["anchor"] == "middle" else "left",
                              e["size"], "fontStyle=1;" if e["bold"] else "",
                              e["color"])

    def _mxgraph(self):
        mx = etree.Element(
            "mxGraphModel", dx="790", dy="517", grid="1", gridSize="10",
            guides="1", tooltips="1", connect="1", arrows="1", fold="1",
            page="1", pageScale="1", pageWidth="850", pageHeight="1100",
            math="0", shadow="0")
        root = etree.SubElement(mx, "root")
        etree.SubElement(root, "mxCell", id="0")
        etree.SubElement(root, "mxCell", id="1", parent="0")
        cid = 2
        for e in self.els:
            k = e["kind"]
            c = etree.SubElement(root, "mxCell", id=str(cid), parent="1")
            if k in ("rect", "text"):
                c.set("value", e["value"])
                c.set("style", self._drawio_style(e))
                c.set("vertex", "1")
                if k == "rect":
                    gx, gy, gw, gh = e["x"], e["y"], e["w"], e["h"]
                else:
                    gw, gh = e["w"], 20
                    gx = e["x"] - gw / 2 if e["anchor"] == "middle" else e["x"]
                    gy = e["y"] - gh / 2
                etree.SubElement(c, "mxGeometry", x=str(gx), y=str(gy),
                                 width=str(gw), height=str(gh),
                                 attrib={"as": "geometry"})
            elif k in ("arrow", "line"):
                c.set("value", "")
                c.set("edge", "1")
                if k == "arrow":
                    c.set("style", "endArrow=classic;html=1;strokeColor=%s;strokeWidth=2;"
                          % e["color"])
                    p1, p2 = (e["x1"], e["y1"]), (e["x2"], e["y2"])
                else:
                    c.set("style", "endArrow=none;startArrow=none;%shtml=1;strokeColor=%s;"
                          % ("dashed=1;" if e["dash"] else "", e["color"]))
                    p1, p2 = (e["x1"], e["y1"]), (e["x2"], e["y2"])
                g = etree.SubElement(c, "mxGeometry", width="50", height="50",
                                     attrib={"relative": "1", "as": "geometry"})
                etree.SubElement(g, "mxPoint", x=str(p1[0]), y=str(p1[1]),
                                 attrib={"as": "sourcePoint"})
                etree.SubElement(g, "mxPoint", x=str(p2[0]), y=str(p2[1]),
                                 attrib={"as": "targetPoint"})
            elif k == "path":
                # drawio 侧用一条无端点相连的折线近似，精确形状以 SVG 为准
                c.set("value", "")
                c.set("edge", "1")
                c.set("style", "endArrow=%s;html=1;strokeColor=%s;strokeWidth=2;"
                      % ("classic" if e["arrow"] else "none", e["color"]))
                g = etree.SubElement(c, "mxGeometry", width="50", height="50",
                                     attrib={"relative": "1", "as": "geometry"})
                nums = [float(n) for n in __import__("re").findall(
                    r"-?\d+(?:\.\d+)?", e["d"])]
                pts = list(zip(nums[0::2], nums[1::2]))[:2]
                for pt, tag in zip(pts, ("sourcePoint", "targetPoint")):
                    etree.SubElement(g, "mxPoint", x=str(pt[0]), y=str(pt[1]),
                                     attrib={"as": tag})
            cid += 1
        return etree.tostring(mx, encoding="unicode")

    def _svg(self, content):
        svg = etree.Element(
            "{%s}svg" % SVG_NS,
            nsmap={None: SVG_NS, "xlink": "http://www.w3.org/1999/xlink"},
            version="1.1", width="%dpx" % self.W, height="%dpx" % self.H,
            attrib={"viewBox": "-0.5 -0.5 %d %d" % (self.W, self.H)})
        svg.set("content", content)
        etree.SubElement(svg, "{%s}title" % SVG_NS).text = self.title
        etree.SubElement(svg, "{%s}desc" % SVG_NS).text = self.desc
        defs = etree.SubElement(svg, "{%s}defs" % SVG_NS)
        mk = etree.SubElement(defs, "{%s}marker" % SVG_NS, id="ptr",
                              markerWidth="9", markerHeight="8", refX="8",
                              refY="4",
                              attrib={"orient": "auto",
                                      "markerUnits": "userSpaceOnUse"})
        etree.SubElement(mk, "{%s}path" % SVG_NS, d="M 0 0 L 9 4 L 0 8 Z",
                         fill=RED)
        g = etree.SubElement(svg, "{%s}g" % SVG_NS)
        for e in self.els:
            k = e["kind"]
            if k == "rect":
                r = etree.SubElement(g, "{%s}rect" % SVG_NS, x=str(e["x"]),
                                     y=str(e["y"]), width=str(e["w"]),
                                     height=str(e["h"]), fill=e["fill"],
                                     stroke=e["stroke"], attrib={"stroke-width": "1"})
                if e["rx"]:
                    r.set("rx", str(e["rx"]))
                if e["value"]:
                    self._svg_text(g, e["x"] + e["w"] / 2,
                                   e["y"] + e["h"] / 2, e["value"], e["size"],
                                   e["bold"], e["color"], "middle", e["font"])
            elif k == "text":
                self._svg_text(g, e["x"], e["y"], e["value"], e["size"],
                               e["bold"], e["color"], e["anchor"], e["font"])
            elif k == "arrow":
                dx = -1 if e["x2"] >= e["x1"] else 1
                p = etree.SubElement(g, "{%s}path" % SVG_NS,
                                     d="M %s %s L %s %s" % (
                                         e["x1"], e["y1"], e["x2"] + dx, e["y2"]),
                                     fill="none", stroke=e["color"],
                                     attrib={"stroke-width": "1.8",
                                             "marker-end": "url(#ptr)"})
            elif k == "line":
                p = etree.SubElement(g, "{%s}path" % SVG_NS,
                                     d="M %s %s L %s %s" % (
                                         e["x1"], e["y1"], e["x2"], e["y2"]),
                                     fill="none", stroke=e["color"],
                                     attrib={"stroke-width": "1"})
                if e["dash"]:
                    p.set("stroke-dasharray", "4 4")
            elif k == "path":
                p = etree.SubElement(g, "{%s}path" % SVG_NS, d=e["d"],
                                     fill="none", stroke=e["color"],
                                     attrib={"stroke-width": str(e["width"])})
                if e["arrow"]:
                    p.set("marker-end", "url(#ptr)")
        return svg

    @staticmethod
    def _svg_text(g, x, y, value, size, bold, color, anchor, font):
        t = etree.SubElement(g, "{%s}text" % SVG_NS, x=str(x), y=str(y),
                             fill=color, attrib={"font-family": font,
                                                 "font-size": str(size),
                                                 "text-anchor": anchor,
                                                 "dominant-baseline": "central"})
        if bold:
            t.set("font-weight", "bold")
        t.text = value

    def save(self, outdir="images"):
        mxstr = self._mxgraph()
        plain = ('<mxfile host="65bd71144e"><diagram id="%s" '
                 'name="Page-1">%s</diagram></mxfile>' % (self.name, mxstr))
        with open("%s/%s.drawio" % (outdir, self.name), "w",
                  encoding="utf-8") as f:
            f.write(plain.replace("><", ">\n<") + "\n")

        # draw.io 内嵌原稿：encodeURIComponent -> deflateRaw -> base64
        payload = urllib.parse.quote(mxstr, safe="~()*!.'")
        comp = zlib.compressobj(9, zlib.DEFLATED, -15)
        b64 = base64.b64encode(
            comp.compress(payload.encode("utf-8")) + comp.flush()).decode()
        content = ('<mxfile><diagram id="%s" name="Page-1">%s'
                   '</diagram></mxfile>' % (self.name, b64))
        svg = self._svg(content)
        etree.ElementTree(svg).write("%s/%s.svg" % (outdir, self.name),
                                     encoding="utf-8", pretty_print=True,
                                     xml_declaration=False)
        return ("%s/%s.drawio" % (outdir, self.name),
                "%s/%s.svg" % (outdir, self.name))


class _Ptr:
    """d.pointer(...).to(x, y) 语法糖：从指针框右/左侧拉一条红箭头。"""

    def __init__(self, d, x, y, w, h):
        self.d, self.x, self.y, self.w, self.h = d, x, y, w, h

    def to(self, tx, ty, label=""):
        cy = self.y + self.h / 2
        if tx >= self.x + self.w:
            self.d.arrow(self.x + self.w, cy, tx, ty, label=label)
        else:
            self.d.arrow(self.x, cy, tx, ty, label=label)
        return self.d
