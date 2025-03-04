from manim import *

class CacheMappingDemo(Scene):
    def construct(self):
        # 定义颜色主题
        colors = {
            "tag": YELLOW,
            "index": BLUE,
            "offset": GREEN,
            "cache_block": PURPLE,
            "memory_block": ORANGE,
        }

        # 第一部分：地址解析的通用结构
        title = Text("缓存地址解析", font_size=36).to_edge(UP)
        address_structure = self.show_address_structure(colors)
        self.play(Write(title), run_time=1)
        self.play(Create(address_structure), run_time=2)
        self.wait(2)

        # 第二部分：直接映射缓存
        self.play(FadeOut(title), FadeOut(address_structure))
        direct_mapped_scene = self.direct_mapped_cache(colors)
        self.play(*direct_mapped_scene)
        self.wait(3)

        # 第三部分：组相联缓存
        self.clear_scene()
        set_associative_scene = self.set_associative_cache(colors)
        self.play(*set_associative_scene)
        self.wait(3)

        # 第四部分：全相联缓存
        self.clear_scene()
        fully_associative_scene = self.fully_associative_cache(colors)
        self.play(*fully_associative_scene)
        self.wait(3)

        # 最终对比总结
        self.clear_scene()
        self.show_comparison_table()

    def show_address_structure(self, colors):
        # 地址位分解示意图
        address_bits = VGroup(
            Rectangle(width=6, height=1, color=WHITE),
            Text("虚拟地址", font_size=24).next_to(Rectangle(), UP)
        )
        tag = Rectangle(width=2, height=1, fill_color=colors["tag"], fill_opacity=0.5)
        index = Rectangle(width=2, height=1, fill_color=colors["index"], fill_opacity=0.5).next_to(tag, RIGHT, buff=0)
        offset = Rectangle(width=2, height=1, fill_color=colors["offset"], fill_opacity=0.5).next_to(index, RIGHT, buff=0)
        labels = VGroup(
            Text("Tag", color=colors["tag"]).scale(0.6).move_to(tag),
            Text("Index", color=colors["index"]).scale(0.6).move_to(index),
            Text("Offset", color=colors["offset"]).scale(0.6).move_to(offset)
        )
        return VGroup(address_bits, tag, index, offset, labels)

    def direct_mapped_cache(self, colors):
        # 直接映射缓存结构
        cache = VGroup(*[Square(side_length=1, color=colors["cache_block"]) for _ in range(8)]).arrange(RIGHT, buff=0.2)
        cache.to_edge(LEFT)
        arrows = VGroup()
        mappings = []
        for i in range(8):
            mem_block = Text(f"M{i}", color=colors["memory_block"]).scale(0.8)
            mem_block.next_to(cache[i], UP)
            arrow = Arrow(mem_block.get_bottom(), cache[i].get_top(), color=WHITE)
            mappings.append(VGroup(mem_block, arrow))
        return [
            Create(cache),
            LaggedStart(*[Create(m) for m in mappings], lag_ratio=0.2),
            Write(Text("直接映射：每个内存块固定映射到一个缓存行", font_size=24).to_edge(DOWN))
        ]

    def set_associative_cache(self, colors):
        # 组相联缓存结构（以2路为例）
        sets = VGroup(*[VGroup(*[Square(side_length=1, color=colors["cache_block"]) for _ in range(2)]).arrange(RIGHT, buff=0.5) for _ in range(4)])
        sets.arrange(DOWN, buff=0.5).to_edge(LEFT)
        mappings = []
        for set_idx in range(4):
            for way in range(2):
                mem_block = Text(f"M{set_idx*2+way}", color=colors["memory_block"]).scale(0.6)
                mem_block.next_to(sets[set_idx][way], UP)
                arrow = Arrow(mem_block.get_bottom(), sets[set_idx][way].get_top(), color=WHITE)
                mappings.append(VGroup(mem_block, arrow))
        return [
            Create(sets),
            LaggedStart(*[Create(m) for m in mappings], lag_ratio=0.1),
            Write(Text("组相联：内存块可映射到指定组内的任意位置", font_size=24).to_edge(DOWN))
        ]

    def fully_associative_cache(self, colors):
        # 全相联缓存结构
        cache = VGroup(*[Square(side_length=1, color=colors["cache_block"]) for _ in range(8)]).arrange_in_grid(4, 2, buff=0.2)
        cache.to_edge(LEFT)
        mappings = []
        for i in range(8):
            mem_block = Text(f"M{i}", color=colors["memory_block"]).scale(0.8)
            mem_block.move_to(UP*2 + RIGHT*i)
            arrow = CurvedArrow(mem_block.get_bottom(), cache[i].get_top(), color=WHITE)
            mappings.append(VGroup(mem_block, arrow))
        return [
            Create(cache),
            LaggedStart(*[Create(m) for m in mappings], lag_ratio=0.2),
            Write(Text("全相联：内存块可以映射到任意缓存位置", font_size=24).to_edge(DOWN))
        ]

    def show_comparison_table(self):
        # 对比表格
        table = Table(
            [["直接映射", "组相联", "全相联"],
             ["固定映射位置", "组内灵活映射", "完全自由映射"],
             ["速度快", "平衡速度与灵活性", "灵活性最高"],
             ["冲突率高", "中等冲突率", "无冲突"]],
            row_labels=[Text("类型"), Text("映射方式"), Text("速度"), Text("冲突率")]
        ).scale(0.6)
        self.play(Create(table), run_time=3)
        self.wait(3)

    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])