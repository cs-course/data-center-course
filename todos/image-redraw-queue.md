# C 语言配图批量重绘队列（2026-11-14）

> 起因：去年首次把 C 语言课堂资料转成 MARP 上线，来不及处理配图，遗留一批老式 PPT/手绘截图。
> 试点 `c-pointer-sub.png → c-pointer-sub.svg` 已验收通过（老大 2026-11-14 确认「按现在做法挺好」）。
> 本文是后续批次的排队单与验收口径。

## 一、范围裁定

全项目讲稿共引用 320 张图（PNG 144 / SVG 66 / JPG 87 / WebP 16 / GIF 5）。**只重绘 C 语言两章的教学示意图**，理由：

| 类别 | 处理 | 原因 |
|---|---|---|
| `c-pointer-*.png`、`c-array-*.png` | **重绘** | 黑底蓝字 PPT 截图 / 蓝手写体内存图，分辨率低、字小、与 gaia 浅色底冲突 |
| `stack-vs-queue.png` | 保留 | 网络插画（非自制素材），`bg right fit` 用得合适 |
| 论文架构图、实验曲线、照片、地图、书封、数据表 | 保留 | 属于引用素材，重绘会丢失原始信息甚至构成篡改 |
| 已有 `*.drawio` + `*.svg` 成对文件（24 组） | 保留 | 去年已处理完 |

**待重绘 24 张**：`c-language-pointer.md` 12 张、`c-language-array.md` 12 张。原 PNG 一律保留作备份，不删除。

## 二、统一规范（沿用试点）

- 产物成对：`images/<name>.drawio`（可编辑原稿）+ `images/<name>.svg`（成品），由 `redraw_kit.py` 从同一份几何描述生成。
- SVG 的 `content` 属性内嵌压缩 drawio 原稿（encodeURIComponent → deflateRaw → base64），用 draw.io 打开 SVG 也能继续改。
- 纯 `<rect>/<path>/<text>`，不依赖 `foreignObject`；带 `<title>/<desc>`。
- 配色：灰内存格 `#CCCCCC`、淡蓝指针框 `#DAE8FC`/`#6C8EBF`、深红箭头 `#C0392B`、浅蓝结论条 `#F2F6FC`、强调格 `#FFFF99`；正文 `#1A1A1A`，标题/结论 `#1F3864`。
- 字体 `Helvetica, Arial, 'Microsoft YaHei', sans-serif`；正文 13–16px，小标题 13px 加粗。
- 每张图至少含：小标题（`①…` / 分节）、主体示意、一条结论说明条。
- **允许教学性重排**：不照抄黑底蓝字；把原图没写清的结论补成说明条；同一组的连续演示必须**共用画布尺寸与坐标**，只改高亮/数值/箭头，形成逐帧效果。
- **不得**改变原图表达的 C 语义（下标、地址、指针运算、字符串结束符位置）；代码/公式抄错比不画更糟。
- md 引用统一改为 `.svg`，显示宽度按下表；`public/` 由脚本同步，不手工散改。

## 三、批次与清单

图元尺寸写作 `画布 W×H → md 显示宽度`。状态：✅ 完成 / ✅ 待办。

### 批次 P1 · 指针内存与地址（6 张，同一 agent，统一画布 300×430）

| # | 原图 | 要点 | 尺寸 | md 显示 | 状态 |
|---|---|---|---|---|---|
| 1 | `c-pointer-concept.png` | `short x` 占 0xFEBC–0xFEBD、`char a[5]` 占 0xFEC0–0xFEC4，变量名即首地址 | 300×430 → w:270 | `c-language-pointer.md` | ✅ |
| 2 | `c-pointer-concept-1.png` | x=1、y=2 各占 2B，p 自己占 4B 并存放 x 首地址 | 300×430 → w:270 | 同上 | ✅ |
| 3 | `c-pointer-concept-2.png` | 直接访问 x / 间接访问 *p，红色弧线从 p 绕回 x 所在格 | 300×430 → w:270 | 同上 | ✅ |
| 4 | `c-pointer-concept-3.png` | `*p` 运算前后 x/y 的值变化 | 300×430 → w:270 | 同上 | ✅ |
| 5 | `c-pointer-concept-3-1.png` | 上帧结果：x=11, y=1 | 300×430 → w:270 | 同上 | ✅ |
| 6 | `c-pointer-type.png` | 0xFEBC 起 CD AB 34 12；*p1=0x1234ABCD、*p2=0xCD，p1+1 走 4B / p2+1 走 1B | 300×430 → w:270 | 同上（引用 2 处） | ✅ |

> 这组 6 张共用同一「内存地址表」底图，逐帧只改高亮格、数值与箭头；`c-pointer-type` 额外画两列对照。

### 批次 P2 · 指针运算与数组（5 张）

| # | 原图 | 要点 | 尺寸 | md 显示 | 状态 |
|---|---|---|---|---|---|
| 7 | `c-pointer-op.png` | `++*px / *++px / *(--px) / *(px--) / *px++ / px+=2` 与 x[5]={1,3,5,7,9} | 320×420 → w:290 | pointer | ✅ |
| 8 | `c-pointer-example.png` | 4 字节 long 逐字节拆高/低 4 位转十六进制字符 | 480×230 → w:620 | pointer（原 `h:350`） | ✅ |
| 9 | `c-pointer-to-array.png` | `a[i]` ⇔ `*(a+i)` ⇔ `*(p+i)` 三种表示 | 360×280 → w:340 | pointer | ✅ |
| 10 | `c-pointer-to-array-1.png` | 指针 p 已走到数组末尾，再 `while(p<a+10)` 是错的 | 360×280 → w:340 | pointer | ✅ |
| 11 | `c-pointer-complex.png` | `int (*p[2])(int)` 声明拆解：函数指针数组 | 520×130 → w:660 | pointer（原 `h:100`） | ✅ |

### 批次 P3 · 字符串与字符数组（6 张）

| # | 原图 | 要点 | 尺寸 | md 显示 | 状态 |
|---|---|---|---|---|---|
| 12 | `c-pointer-strsort.png` | 「比的是元素，排的是指针」：strcmp 比较内容、交换指针数组元素 | 380×260 → w:350 | pointer | ✅ |
| 13 | `c-array-strcmp.png` | S=`abcabcabdabba\0`（14 格）、T=`abcabd\0`（7 格），逐字符比较，S[5]=c < T[5]=d | 400×190 → w:360 | array | ✅ |
| 14 | `c-array-strstr-1.png` | strstr 逐帧 ①：S 与目标串 T 初始对齐 | 400×190 → w:460 | array | ✅ |
| 15 | `c-array-strstr-2.png` | 逐帧 ②：T 右移 1 格，首字符失配 | 400×190 → w:460 | array | ✅ |
| 16 | `c-array-strstr-3.png` | 逐帧 ③：T 右移 2 格，首字符失配 | 400×190 → w:460 | array | ✅ |
| 17 | `c-array-strstr-4.png` | 逐帧 ④：T 右移 3 格，6 位全匹配，返回下标 3 | 400×190 → w:460 | array | ✅ |

> 13–17 共 5 张**共用 400×190 画布、同一套 S 行坐标**（x0=52、步长 22、14 格），T 行 x0 = 52/52/74/96/118 逐帧右移 1 格。
> 原讲稿把 4 帧挤在右栏 `3fr 1fr` 里，改 SVG 后第 4 帧被底边裁掉；已把四帧移到新增的独立页（2×2 满版，各 w:460），代码页只留首帧。array 讲稿因此 76 → 77 页。

### 批次 P4 · 数组与算法（7 张）

| # | 原图 | 要点 | 尺寸 | md 显示 | 状态 |
|---|---|---|---|---|---|
| 18 | `c-array-2d.png` | `short x[2][3]` 行优先，0xffd0 起步长 2B，值 85/91/88/82/95/88（与讲稿正文一致） | 300×400 → w:280 | array | ✅ |
| 19 | `c-array-access.png` | a[0]..a[3] 连续存放、数组名即首地址；步长按同页 `int a[4]` 改为 **4B**（原图标 8B，与讲稿冲突，已修正） | 260×430 → w:250 | array | ✅ |
| 20 | `c-array-as-parameter.png` | 形参 x/y 与实参数组 2 3 5 6 7 的传递 | 320×230 → w:300 | array | ✅ |
| 21 | `c-array-map.png` | 一维数组映射到连续内存条 | 260×360 → w:250 | array | ✅ |
| 22 | `c-array-bubblesort.png` | `10 8 5 7` 升序三轮：比较 3/2/1 次，交换 3/2/0 次 | 420×430 → w:380 | array | ✅ |
| 23 | `c-array-partition.png` | `v[]={6,5,2,4,7,3,1,8}` 选 4 为切分元素，三步归位到 `1 2 3 4 7 5 6 8` | 420×330 → w:700 | array（原 `bg fit`，改普通插图） | ✅ |
| 24 | `c-array-binarysearch.png` | `8 13 21 28 35 41 52` 中找 x=14，mid=3→1，14 不在表中 | 460×190 → w:560 | array（原 `h:270`） | ✅ |

## 四、验收标准

1. `etree.parse()` 校验两个 XML；SVG 的 `content` 可解压缩回 `mxGraphModel`。
2. 用 headless Edge 把新 SVG 按目标显示宽度渲染，逐张确认：文字无裁切/溢出、中文正常、箭头指向正确格子、结论条可读。
3. 同一组的连续帧并排比对，坐标不跳变。
4. 实际编译目标页截图，确认图片在 gaia 版心内、不裁切、字号可读。
5. md 引用全部指向 `.svg`；`public/images/` 同步；受影响的两份 `public/*.html` 用 MARP 整体重编译，无残留旧 PNG 引用。
6. 验收阶段保留原 PNG 作为回退；全部核验通过后再按白名单清理（见第七节）。

## 五、执行记录（2026-11-14 完成）

- **流水线固化**：新增 `redraw_kit.py`（`Diagram` 类），从一份几何描述同时产出 `.drawio` 与 `.svg`，SVG `content` 内嵌压缩原稿。后续再重绘图一律用它，不再手写 SVG。
- **并行分工**：P1/P2/P3/P4 四批各由一个子任务独立完成，共用同一工具库与规范；24 组 48 个文件全部生成。
- **实图校正**（我给的初版要点有误，各批以放大后的原图为准，已回填上表）：
  - 内存地址实为 `0xFEBC / 0xFEBD / 0xFEC0–0xFEC4`，不是 `bf9C / 8f80` 系列。
  - 字符串实为 `S=abcabcabdabba\0`、`T=abcabd\0`；`c-array-strcmp.png` 与 `c-array-strstr-1.png` 原文件 md5 相同。
  - `c-array-2d` 的值 85/91/88/82/95/88 与 `c-language-array.md:374` 正文一致。
  - **主动修正一处讲稿冲突**：`c-array-access` 原图标「8B 步长」，同页代码是 `int a[4]`；已改为 `4B (int)`，SVG 正文、`drawio` 与内嵌 `content` 三处同步。
- **版式修复**：`c-array-strstr-1..4` 原本四张挤在 `3fr 1fr` 右栏，换成 400×190 的 SVG 后第 4 帧被底边裁掉。新增独立页做 2×2 满版对照（各 `w:460`），代码页只留首帧；array 讲稿 76 → 77 页。另把 `c-pointer-example`、`c-pointer-complex`、`c-array-partition`（原 `bg fit`）、`c-array-binarysearch` 由 `h:`/`bg` 改成合适宽度。
- **验收**：48 个 XML 全通过；四批总览截图 + 8 张真实幻灯片截图逐张复核；发布页 `public/c-language-array.html#49` 与本地预览 md5 完全一致。
- **发布同步**：`public/c-language-pointer.html`（109→110 页，含今天早些时候的「指针与 AI」插页）与 `public/c-language-array.html`（76→77 页）已用 MARP 整体重编译；48 个新文件已同步到 `public/images/`。原 PNG 在验收阶段全部保留，之后按第七节清理。

## 六、已知环境约束与剩余事项

- 当前 shell 无 `rsync`，完整 `bash compile.sh` 跑不通；本轮改用 `bin/marp <md> --no-stdin -o public/<md>.html` 定向重编译受影响的两份 HTML，其余 33 份 HTML 未动。
- `bin/marp` 非交互调用需加 `--no-stdin`，且路径用 POSIX 形式；headless Edge 截图可用 `#页码` 锚点直达目标页。
- 有 rsync 的 Git Bash/MSYS2 里仍建议跑一次完整 `compile.sh` 做全站一致性重建（会重建全部 35 份 HTML，产生 lang/scope churn，但内容等价）。

## 七、旧 PNG 清理（2026-11-14 完成）

- **没有直接跑 `clean_unused_images.sh`**：只读复现表明它会 `git rm` 96 张，而本次要清的只有 25 张。其余 71 张里 65 张是 `china-datacenter-panorama-2026.md`（22）、`huawei-ascend-supernode-photos.md`（15）、`ulanqab-datacenter-photos.md`（11）、`memory-hierarchy.html`（12）等**素材清单文档**登记的备用照片——这些文档只列文件名、不嵌图，脚本的「未引用＝无用」假设在本仓库不成立；另 6 张为完全零引用的历史素材。两者均保留。
- 脚本其它问题：只扫根目录 `*.md`（漏 `todos/` 9 处引用、`public/*.html`、`demos/*.html`）；只认 `![](...)` / `<img src="...">`；第二行 `sed -E 's/.*$$([^)]*)$$.*/\1/'` 是死代码；无 dry-run / 确认 / 备份；`public/` 是独立仓库，`git rm` 根本删不到 `public/images/` 的旧副本。
- **执行方式**：按 25 张白名单，分 3 批（10/10/5）在两个仓库各执行 `git rm`，共 50 个文件；每批验证文件消失。删除前确认真实图片引用残留 0、两仓库目标文件无未提交改动（git 历史可完整恢复）。
- **备份**：`D:/documents/portforlio/Course/cs-courses-image-backup-20261114/`（仓库外），含 `repo/images/`、`public/images/` 各 25 张与 `MANIFEST.txt`（路径、字节数、sha256、两仓库 HEAD、恢复方式）。50 个文件 sha256 逐一比对一致。
- **删除后回归**：全项目 `*.html` / `*.md` 对旧 PNG 的引用残留 0；25 组新 SVG 在两处齐全；`public/c-language-array.html#49` 截图确认四帧矢量图正常加载（49 of 77）。`images/` 与 `public/images/` 各剩 390 张图。
- `todos/image-redraw-queue.md` 表格里的 `` `xxx.png` `` 是历史记录，指向已删除文件属预期，保留不改。
- 两个 git 仓库（根目录、`public/`）的改动均未提交，留给老大审查后手动 push。
