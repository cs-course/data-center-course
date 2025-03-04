from manim import *
import random

class CacheReplacementDemo(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 颜色定义
        self.COLORS = {
            "hit": GREEN,
            "miss": RED,
            "cache_block": BLUE,
            "text": WHITE
        }
        # 缓存大小定义
        self.cache_size = 4

    def construct(self):
        # 全局参数
        access_sequence = [1, 2, 3, 4, 1, 5, 1, 2]  # 可替换为其他测试序列
        
        # 创建初始缓存状态
        cache = self.create_cache(self.cache_size)
        access_flow = self.create_access_flow(access_sequence)
        self.play(Create(cache), Create(access_flow))
        self.wait(1)

        # 三种策略对比演示
        strategies = ["LRU", "FIFO", "Random"]
        strategy_scenes = [
            self.lru_strategy(cache.copy(), access_sequence.copy()),
            self.fifo_strategy(cache.copy(), access_sequence.copy()),
            self.random_strategy(cache.copy(), access_sequence.copy())
        ]

        for i, strategy in enumerate(strategy_scenes):
            title = Text(f"策略: {strategies[i]}", font_size=36).to_edge(UP)
            self.play(Write(title))
            self.play(*strategy["animations"])  # 使用 * 解包动画列表
            self.show_performance_stats(access_sequence, strategy["hits"], strategy["replacements"])
            self.wait(2)
            self.clear_scene()

        # 实际应用场景分析
        self.real_world_scenarios()

    def create_cache(self, size):
        # 创建缓存可视化模块
        blocks = VGroup()
        for i in range(size):
            block = Square(side_length=1, color=self.COLORS["cache_block"])
            label = Text(f"Block {i+1}", font_size=20).move_to(block)
            blocks.add(VGroup(block, label))
        blocks.arrange(RIGHT, buff=0.5).shift(UP)
        return blocks

    def create_access_flow(self, sequence):
        # 创建访问序列可视化
        elements = [Text(str(num), font_size=24) for num in sequence]
        flow = VGroup(*elements).arrange(RIGHT, buff=0.3).shift(DOWN)
        return flow

    def lru_strategy(self, cache, sequence):
        # LRU策略动画
        used_order = []
        hits = 0
        replacements = 0
        animations = []
        
        for i, num in enumerate(sequence):
            # 命中检测动画
            hit, anims = self.highlight_access(cache, num)
            animations.extend(anims)
            if hit:
                used_order.remove(num)
                used_order.append(num)
                hits += 1
            else:
                # 替换动画
                if len(used_order) >= self.cache_size:
                    lru = used_order.pop(0)
                    anims = self.replace_block(cache, lru, num)
                    animations.extend(anims)
                    replacements += 1
                else:
                    anims = self.add_new_block(cache, num)
                    animations.extend(anims)
                used_order.append(num)
        return {"hits": hits, "replacements": replacements, "animations": animations}

    def fifo_strategy(self, cache, sequence):
        # FIFO策略动画
        queue = []
        hits = 0
        animations = []
        
        for num in sequence:
            hit, anims = self.highlight_access(cache, num)
            animations.extend(anims)
            if hit:
                hits += 1
            else:
                if len(queue) >= self.cache_size:
                    oldest = queue.pop(0)
                    anims = self.replace_block(cache, oldest, num)
                    animations.extend(anims)
                else:
                    anims = self.add_new_block(cache, num)
                    animations.extend(anims)
                queue.append(num)
        return {"hits": hits, "replacements": len(queue)-self.cache_size, "animations": animations}

    def random_strategy(self, cache, sequence):
        # 随机策略动画
        current_blocks = []
        hits = 0
        animations = []
        
        for num in sequence:
            hit, anims = self.highlight_access(cache, num)
            animations.extend(anims)
            if hit:
                hits += 1
            else:
                if len(current_blocks) >= self.cache_size:
                    victim = random.choice(current_blocks)
                    anims = self.replace_block(cache, victim, num)
                    animations.extend(anims)
                    current_blocks.remove(victim)
                else:
                    anims = self.add_new_block(cache, num)
                    animations.extend(anims)
                current_blocks.append(num)
        return {"hits": hits, "replacements": len(current_blocks)-self.cache_size, "animations": animations}

    def highlight_access(self, cache, num):
        # 高亮显示访问过程
        animations = []
        for block in cache:
            if block[1].text == str(num):
                animations.append(block.animate.set_color(self.COLORS["hit"]))
                animations.append(block.animate.set_color(self.COLORS["cache_block"]))
                return True, animations
        animations.append(Flash(cache[0], color=self.COLORS["miss"]))  # 假设 cache 不为空
        return False, animations

    def replace_block(self, cache, old_num, new_num):
        # 执行替换动画
        animations = []
        for block in cache:
            if block[1].text == str(old_num):
                new_label = Text(str(new_num), font_size=20).move_to(block[1])
                animations.append(Transform(block[1], new_label))
                return animations
        return animations

    def add_new_block(self, cache, num):
        # 添加新块动画
        animations = []
        for block in cache:
            if block[1].text.startswith("Block"):  # 假设初始块标签为 "Block 1", "Block 2", ...
                new_label = Text(str(num), font_size=20).move_to(block[1])
                animations.append(Transform(block[1], new_label))
                return animations
        return animations

    def show_performance_stats(self, sequence, hits, replacements):
        # 显示性能指标
        stats = VGroup(
            Text(f"访问次数: {len(sequence)}", font_size=24),
            Text(f"命中次数: {hits}", color=self.COLORS["hit"]),
            Text(f"替换次数: {replacements}", color=self.COLORS["miss"])
        ).arrange(DOWN).to_edge(RIGHT)
        self.play(Write(stats))
        self.wait(2)

    def real_world_scenarios(self):
        # 实际应用场景分析
        title = Text("现代应用中的替换策略挑战", font_size=36).to_edge(UP)
        self.play(Write(title))

        scenarios = VGroup(
            Text("1. 图遍历算法（随机访问模式）", font_size=24),
            Text("2. 矩阵运算（顺序访问模式）", font_size=24),
            Text("3. 流式数据处理（时序相关性）", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP*0.5)

        questions = VGroup(
            Text("- LRU是否适合突发访问模式？", color=YELLOW),
            Text("- 如何设计混合替换策略？", color=YELLOW),
            Text("- 机器学习能否预测访问模式？", color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT).shift(DOWN*0.5)

        self.play(Write(scenarios), run_time=2)
        self.wait(1)
        self.play(Write(questions), run_time=2)
        self.wait(3)

    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])