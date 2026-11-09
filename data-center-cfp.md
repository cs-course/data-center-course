---
marp: true
theme: gaia
title: 数据中心技术 · HUSTDS 2026 征稿
# size: 4:3
paginate: true
---

<!--
  放置位置：cs-courses 根目录，文件名 data-center-cfp.md
  编译：./compile.sh（内部执行 bin/marp *.md），产物 public/data-center-cfp.html
  发布：https://marp-public.pages.dev/data-center-cfp
  关联：写作包放在 cs-courses/files/，由 compile.sh 的 files 通道同步到站点
-->

<!-- _class: lead -->

# HUSTDS 2026 征稿

**数据中心技术 · 课程报告（占 40%）**

施展
武汉光电国家研究中心，计算机学院

2026-11-13

---

## 课程报告40分怎么拿？

<style scoped>
  li, p {
    font-size: 28px;
  }
</style>

不是交一份作业，是**投一次稿**：

- 按研讨选篇所属方向，自选一个真问题 → 匿名写成 4–6 页 → 投进 CMT
- 你会收到 **2–3 份同学评审 + 1 份教师元评审**（80 人一人一份，有 8 篇会多一份）
- 你也要给别人评 1 篇，**评审本身计 10 分**
- 12-25 课堂公布决定：Oral / Poster / Major Revision

> 流程体验真实，后果不做惩罚——没有「因为写得一般被拒」这回事

---

## 时间表

<style scoped>
  td, th, p {
    font-size: 25px;
  }
</style>

| 日期 | 事项 | 谁 |
| :---: | :--- | :---: |
| 11-13 | CFP 发布，CMT 开放投稿 | Chair |
| 11-27 | 分组定稿（36 组），完成注册 | 各组 |
| **12-04** | **题目与摘要登记截止**（不登记无法进入分派） | 各组 |
| 12-06 ~ 12-10 | 评审意向（bidding） | 全体 |
| **12-13** | **全文截止**（12-13 23:59） | 各组 |
| 12-14 ~ 12-20 | 评审期 | 全体 |
| **12-25** | **决定公布**（课堂） | Chair |
| 12-31 | 终稿上传（camera-ready） | 各组 |

---

## 写什么：一个真问题

<style scoped>
  li, p {
    font-size: 24px;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.4rem;
  }
  .good {
    color: #1a7f37;
  }
  .bad {
    color: #b00;
  }
</style>

<div class="columns">

<div>

<p class="good"><strong>合格</strong></p>

- 说清**一个**具体问题，不是「XX 技术综述」
- ≥15 篇文献，≥8 篇近三年顶会（FAST/ATC/OSDI/SOSP/ISCA/HPCA…）
- 有**对比框架**：一张分类表胜过三段形容词
- 有**判断**：哪条路线会赢、什么条件下翻盘
- 指出**你自己觉得最难**的那个开放问题

</div>

<div>

<p class="bad"><strong>不合格</strong></p>

- 只有罗列没有框架
- 只有结论没有依据
- 只有定性没有数字
- 参考文献里查不到的条目
- 摘要写「具有重要意义」

</div>

</div>

---

## 写作包：只给 LaTeX

<style scoped>
  li, p, td {
    font-size: 23px;
  }
</style>

**没有 Word 版**——不是偏好，是训练目标：匿名、页数、交叉引用、文献管理，LaTeX 在写的时候就管住，Word 要交之前才发现。

| 包内 | 用途 |
| :--- | :--- |
| 主模板 | `paper/hustds2026-paper.tex`，从这一份开始写（匿名投稿版） |
| 范文 | `example/` 5 页可编译样例，不知「分析」怎么写时看它 |
| 训练任务 | `02-训练任务.md` 六关约 2 小时，练的就是你要交的这篇 |
| 速查 | `04-LaTeX速查.md` 报错对照表 + 抄了就用 |
| 智能体协作 | `05-智能体协作.md` 装环境、排错、画图、查文献的提示词 |

下载 <https://marp-public.pages.dev/files/hustds2026-latex-kit.zip>

---

## 怎么投：三条硬规矩

<style scoped>
  li, p {
    font-size: 26px;
  }
</style>

1. **4–6 页，单栏**，用写作包里的 `paper/hustds2026-paper.tex`
2. **双盲**：姓名、学号、邮箱、导师、致谢、基金号，一个都不能留
   - CMT 的 Authors 字段要如实填（只有我看得到，用于回避分派）
3. **参考文献逐条核实**——AI 编的文献是最严重的错误

交稿前跑一遍自检：

```bash
python tools/check_submission.py --pdf my-paper.pdf
```

---

## 你也要评别人

<style scoped>
  td, th, p, li {
    font-size: 26px;
  }
</style>

每人 1 篇，12-20 前提交。评审占 **10 分**：

| 项 | 分 | 什么叫做到 |
| :--- | :-: | :--- |
| 及时 | 3 | 12-20 前提交 |
| 定位准确 | 3 | 指明页码 / 节号 / 图表号 |
| 建议可执行 | 2 | 改哪、补什么、删什么 |
| 事实与口味分离 | 2 | 区分「这里错了」与「我不喜欢」 |

> 「结构完整、分析不足」——这种评语 0 分

---

## 三个坑

<style scoped>
  li, p {
    font-size: 26px;
  }
</style>

1. **匿名没做干净**：PDF 属性里的作者名、图注里的「我们组」、截图里的用户名、致谢忘了删
2. **页数踩线**：6 页是硬上限，图表也算；压缩先删例子，别删分析
3. **AI 幻觉文献**：查不到的条目一律删，这比少引两篇严重得多

---

<!-- _class: lead -->

<style scoped>
  p, li {
    font-size: 26px;
  }
</style>

## 下一步

**本周**：组队定稿 → 注册 CMT → 想清楚一个问题
**12-04 前**：题目和摘要登记进 CMT

投稿入口 <https://cmt3.research.microsoft.com/HUSTDS2026/>
写作包 <https://marp-public.pages.dev/files/hustds2026-latex-kit.zip>
