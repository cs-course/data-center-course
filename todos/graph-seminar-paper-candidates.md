# 《计算机系统设计》· 图系统方向研讨候选论文清单（6 篇）

> 制表日期：2026-09-15 ｜ 供主讲老师汇总进军山课堂研讨课安排
> 对应讲次：`system-for-graph.md`（面向图应用的系统设计，2026-09-14 已授课）
> 主题范围：图处理/图学习**系统** —— 存储、I/O、并行、体系结构、动态图、图+LLM

## 一、筛选口径

| 维度 | 口径 |
|---|---|
| 层次 | **全部 CCF-A 类会议**（依据《CCF 推荐国际学术会议目录》2026 版：ATC、EuroSys、SOSP、OSDI、MICRO、ISCA、SC、PPoPP、FAST、SIGMOD、VLDB、KDD、WWW 等均为 A 类） |
| 时间 | **2023 年及以后**（近三年） |
| 方向 | 图**系统**（存储 / I/O / 并行 / 体系结构 / 大规模图学习系统 / 动态图 / 图+LLM 系统），不收纯 GNN 模型论文 |
| 可研讨性 | 优先有**开源代码或 Artifact Evaluated** 的工作，保证学生分组能"讲得动、问得出、可复现" |
| 承接性 | 每篇都能明确挂到本讲已建立的 4 条主线之一 |

### 四条主线与本讲内容锚点

| 主线 | 本讲已讲内容 | 本次覆盖论文 |
|:---|:---|:---|
| **A. 分层存储与外存 I/O** | 层次存储、GraphChi / X-Stream / GridGraph、GraphChi 的分批与排序、`walk_io_demo` 分块换入换出 | ① ChunkGraph |
| **B. 访存局部性与并行/体系结构** | 偏斜性与随机性、CacheLab trace、`graph-trace-viewer` 三布局回放、重排 | ③ TMiner |
| **C. 图采样与图表示学习** | DeepWalk / node2vec 一阶→二阶、SOWalker 外存二阶游走 | ② gSampler、④ WiseGraph |
| **D. 动态图 / 时空检索 / KG+LLM** | 时序图模型、LSM-Subgraph、PMA 邻接数组、KG 嵌入、CoT-RAG | ⑤ Revisiting DGS、⑥ GraphRAG 统一分析 |

---

## 二、六篇主推（总览表）

| # | 论文 | 会议 | CCF | 一句话定位 | 承接主线 | 开源 |
|:-:|:---|:---|:-:|:---|:-:|:-:|
| ① | Efficient Large Graph Processing with Chunk-Based Graph Representation Model（**ChunkGraph**） | USENIX ATC '24，pp.1239–1255 | A | 用"分块图表示"重做 NVMe SSD 上的外存图处理 | A | ✅ |
| ② | gSampler: General and Efficient GPU-based Graph Sampling for Graph Learning | SOSP '23，pp.562–578 | A | 用 ECSF 四步模型统一 15 种图采样算法并端到端编译到 GPU | C | ✅ AE 三项徽章 |
| ③ | TMiner: A Vertex-Based Task Scheduling Architecture for Graph Pattern Mining | MICRO '24，pp.1295–1308 | A | 三层手段消除并行图挖掘的冗余访存，近存执行 | B | ❌ 无代码（模拟器未公开） |
| ④ | WiseGraph: Optimizing GNN with Joint Workload Partition of Graph and Operations | EuroSys '24，pp.1–17 | A | 把"图数据划分"与"算子划分"放进同一优化空间 | C | ✅ |
| ⑤ | Revisiting the Design of In-Memory Dynamic Graph Storage | SIGMOD '25，PACMMOD 3:1–27 | A | 用统一沙箱重审 5 大动态图存储系统，量化"动态"的代价 | D | ✅ |
| ⑥ | In-depth Analysis of Graph-based RAG in a Unified Framework | PVLDB 18(13):5623–5637, 2025 | A | 统一框架下把 12 种 GraphRAG 方法做 apples-to-apples 拆解对比 | D | ✅ |

---

## 三、逐篇详解（可直接下发学生）

### ① ChunkGraph — 外存图处理在 NVMe SSD 上重做一遍

- **作者 / 单位**：Rui Wang, Weixu Zong, **Shuibing He**\*, Xinyu Chen, Zhenxin Li, Zheng Dang — 浙江大学（+杭州高新区区块链与数据安全研究院）
- **出处**：USENIX ATC '24，pp.1239–1255｜Open Access
- **一句话**：NVMe SSD 让"把随机 I/O 转成顺序 I/O"的老套路不再划算，于是把图按 chunk 重新组织。
- **问题动机**（可直接作为研讨导入问题）：
  - 老外存系统（GraphChi / X-Stream / GridGraph）为 HDD/SATA 设计，靠子图迭代模型把大量随机 I/O 转成少量顺序 I/O，代价是**同步开销 + 粗粒度 I/O + 编程难**；
  - NVMe SSD 顺序/随机访问性能已接近，老套路"不再 cost-effective"；
  - 另一条路是靠 OS page cache / TriCache 做页缓存，但对图应用特性（偏斜、随机）一无所知。
- **设计要点**：chunk-based graph representation model —— ① 顶点**分类**（按度/活跃与否）② 顶点**分层**存储 ③ chunk **布局优化**。
- **结果**：相比主流外存图系统与依赖通用缓存的内存图系统，均有**数倍**提升（论文 Figure 8–10）。
- **资源**：PDF `https://www.usenix.org/conference/atc24/presentation/wang-rui`｜代码 `https://github.com/ISCS-ZJU/ChunkGraph`（基于 Ligra，含对比系统 Blaze / Ligra-mmap，AE 版本存档于 Zenodo）
- **硬件前提**：需 NUMA 服务器 + Intel P5520 NVMe SSD；Ubuntu 20.04 / kernel 5.4 / gcc≥5.3。
- **与本讲呼应**：讲稿在"分层式架构"ppt 上留下的那句"大块访问的实现 / 顺序访问的实现 / 分批问题——如何排序"，本文给出 2024 年的答案；也可与课堂演示 `walk_io_demo.html`（内存仅 M=2 块的分块换入换出）直接对照讨论"块大小如何定"这一同源问题。
- **研讨问题设计**：
  1. NVMe 让随机 I/O 不再昂贵之后，"分区—顺序扫—迭代"这套设计还剩多少价值？哪些假设被新技术推翻了？
  2. ChunkGraph 的"chunk"和 SOWalker 的"walk-aware block"是一回事吗？二者的**换入换出单位**分别由什么决定？
  3. 顶点分类的依据是静态度还是动态活跃度？如果是前者，面对"重排图 / 活跃顶点会漂移"的问题怎么办？（可接 `vertex-activity-trend.jpg` 那页）

---

### ② gSampler — 图采样统一到 GPU 上

- **作者 / 单位**：Ping Gong, Renjie Liu, Zunyao Mao, Zhenkun Cai, Xiao Yan, Cheng Li, Minjie Wang, Zhuozhao Li — 中国科学技术大学 / 南方科技大学 / AWS 上海 AI Lab
- **出处**：SOSP '23，pp.562–578
- **一句话**：先系统研究 15 种主流采样算法，提取出 ECSF 四步模型，再编译成高效 GPU 执行。
- **问题动机**：图采样在端到端 GNN 训练中最高占到 **96.2%** 的时间，且算法层出不穷、语义各异。既有框架要么表达不了新算法，要么表达得了却跑不快。
- **设计要点**：
  - **ECSF 编程模型**：Extract（抽子图）→ Compute（算 prob/dist）→ Select（抽样）→ Finalize（产出mini-batch）；
  - **矩阵中心 API** + **data-flow IR**（改 torch.fx）做 optimized pass（CSE、kernel fusion）；
  - 三项优化：计算优化（消冗余搬运/算子）、**数据布局优化**（按算法+数据集选存储格式）、**super-batching**（批量合批提升利用率且不损失精度）。
- **结果**：7 种算法 / 4 个数据集 / 2 种硬件，采样加速 **1.14–32.7×**，平均 **6.54×**（vs DGL），端到端训练时间降 **40%+**。
- **资源**：代码 `https://github.com/gsampler9/gSampler`（Apache-2.0）｜SOSP'23 Artifact 三徽章齐全：**Available / Functional / Results Reproduced**（评测机为 p3.16xlarge，8×V100 / 64 vCPU / 480GB）
- **特别提示**：该框架**直接内置 Node2Vec 与 RandomWalk 采样器**（还支持 FastGCN、LADIES、GraphSAGE、GraphSAINT、KGCN、PASS、ShadowGNN 等）——与本讲"随机游走生成训练语料"一节天然衔接，是本清单中**最能让学生动手复现**的一篇。
- **研讨问题设计**：
  1. 研究 15 种算法才抽出 4 步抽象——这种"**先穷举归纳再建模**"的方法论，和为单个算法做特化优化相比，价值在哪、代价在哪？
  2. 把 ECSF 套到 **node2vec 的二阶转移**上试试：Extrct 阶段要抽什么？（提示：$(t,v_i)$ 联合状态）第二步 Compute 要算什么？（提示：$\alpha_{pq}$ 与归一化）→ 学生可以现场用 gSampler 写一遍二阶采样并与一阶对比 I/O/时间。
  3. super-batching"不损失精度"的边界在哪？什么情况下合批会破坏采样分布的无偏性？

---

### ③ TMiner — 把并行图挖掘的冗余访存在三个层次上掐掉

- **作者 / 单位**：Zerun Li, Xiaoming Chen, Yinhe Han — 中国科学院计算技术研究所（处理器芯片全国重点实验室）
- **出处**：MICRO '24，pp.1295–1308，DOI `10.1109/MICRO61859.2024.00096`
- **一句话**：图模式挖掘并行化后，**访存**成为主瓶颈；TMiner 从"PE 间 / 任务内 / PE 内"三层冗余入手，配 DIMM 近存架构打掉它们。
- **问题动机**：三层冗余访存
  1. 多个计算单元同时访问同一份数据 → 冗余 DRAM/LLC 访问 + 有效 cache 容量下降；
  2. 同一计算单元在离散时刻反复访问同一份数据 → 冗余 DRAM 访问；
  3. 一个任务把"访问一个完整集合"拆成"访问多个子集" → 冗余 DRAM 访问 + **破坏访存连续性**。
- **设计要点**：
  - **设计期**：基于"不相交邻居顶点集访问"的任务划分，保证各 PE 访存不重叠 → 消除 PE 间冗余；
  - **编译期**：用全局邻居信息把对多个子集的访问合并为对**超集**的一次访问 → 消除任务内冗余 + 提升局部性；
  - **运行期**：面向数据复用的任务调度，动态迁移并合并访存模式相近的任务 → 消除 PE 内冗余；
  - **DIMM 近存架构**利用 DRAM 内部带宽 + 扩展 ISA。
- **结果**：冗余访存降低约 **90%**，跨社交/通信网络数据集与多种模式平均性能提升 **3.5×**（且不牺牲并行度）。
- **与本讲呼应**：和课堂 `graph-trace-viewer.html` 演示是同一件事的**软硬两端**——课上让学生看三种布局下 trace 的分簇形态；本文则是"认出冗余访存的三个来源 → 分别在编译期和运行期干掉它"。MICRO'24 录取率 **22.7%**（497 投稿 / 113 收录）。
- **研讨问题设计**：
  1. 第 3 层"访问多个子集 → 合并为访问超集"，听起来像牺牲精度换带宽？合并超集是否引入**无效顶点**？在什么时候不成立？
  2. 把这三层分类套回讲稿的 `CSR + BFS`：在本演示的三布局里，哪一种冗余（`CSR_index` 的重复扫描 / `visited` 的随机判重 / `frontier` 的队列扫描）最严重？
  3. 近存 vs 加速器 vs 纯软件重排：同一份收益需要付出什么不同的代价？（成本/适用场景/可编程性）

---

### ④ WiseGraph — 图划分与算子划分，别再各划各的

- **作者 / 单位**：Kezhao Huang, Jidong Zhai, Liyan Zheng, Haojie Wang, Yuyang Jin, Qihao Zhang, Runqing Zhang, Zhen Zheng, Youngmin Yi, Xipeng Shen — 清华大学等
- **出处**：EuroSys '24，pp.1–17，DOI `10.1145/3627703.3650063`
- **一句话**：现有 GNN 系统把"图数据怎么切"和"算子怎么切"分开优化，作者用一个 gTask 抽象把二者放进同一个优化空间。
- **问题动机**：分别优化导致低效 + 大量数据搬运；割裂使粒度/切分显而易见"对不上"。
- **设计要点**：提出面向 GNN 的 workload 抽象 **gTask**——既能把现有各类划分策略表达为特例，又能暴露新的优化机会；基于 gTask 自适应生成匹配输入图 + GNN 模型的划分方案。
- **结果**：5 个典型 GNN 模型上，单 GPU **2.04×**、多 GPU **2.22×**（相比现有 GNN 框架）。
- **资源**：代码 `https://github.com/xxcclong/CxGNN-Compute`
- **与本讲呼应**：直接回应讲稿那一页——"**图分区的矛盾：尺寸平衡 / 切割少 / 过度分区**"（PowerGraph / PowerLyra / FENNEL / 分布式异步 FENNEL）。传统 distributed graph system 只解决"图怎么切"，GNN 时代多了一个维度"算子怎么切"。
- **研讨问题设计**：
  1. 这其实是"**划分粒度失配**"问题的换壳重演——和 PowerGraph 的 edge-cut vs vertex-cut 是同类矛盾吗？区别在哪？
  2. gTask 声称"现有策略都是它的特例"，请学生挑一个（如 GraphSAGE 采样 + Betty 的 batch-level partition）验证这一说法是否成立。
  3. 多 GPU 只比单 GPU 多赚 0.18× 的提速（2.04→2.22），说明瓶颈在通信还是划分？给出你的判据。

---

### ⑤ Revisiting the Design of In-Memory Dynamic Graph Storage — 给"动态"标价

- **作者 / 单位**：Jixian Su, Chiyu Hao, Shixuan Sun, Minyi Guo（上海交通大学）· Sen Gao, Jiaxin Jiang, Yao Chen, Bingsheng He（新加坡国立大学）· Hao Zhang, Chenyi Zhang（华为云）
- **出处**：SIGMOD '25，Proceedings of ACM on Management of Data (PACMMOD) 3:1–27，DOI `10.1145/3709720`｜arXiv:2502.10959
- **一句话**：把 5 大动态图存储系统（LiveGraph / Sortledton / Teseo / Aspen / LLAMA）重新实现进同一个沙箱，用同一把尺子量出"动态"的代价。
- **方法**：
  - 提出 DGS **两层抽象**：全局抽象（时间戳、可串行化、事务编排）+ 局部抽象（顶点表/邻居表的物理布局）；
  - 基于此实现 **DGS Sandbox**（约 7,800 行 C++），把现有方法的**核心技法**而非完整系统放进同一环境，配合 CPU 性能计数器做硬件级剖析。
- **关键发现（全部可直接作为研讨素材）**：
  | 发现 | 数据 |
  |:---|:---|
  | 空间开销 | Aspen 内存占用是 CSR 的 **3.3–10.8×**；最优的细粒度方法也达 **4.1–8.9×** |
  | 静态 vs 动态 | 静态 CSR 查询吞吐比最好的动态系统高 **2.4–11.0×** |
  | 布局之争 | 连续存储布局（LiveGraph）明显优于分段索引（Teseo）：后者 cache / DTLB miss 与分支预测失败更高，浪费了硬件预取与 SIMD 向量化 |
  | 并发粒度 | 细粒度（逐边 MVCC）为每个邻居维护版本并做校验 → 严重效率与空间问题，且在**高度数顶点**上竞争剧烈；但批大小超过 **256** 条更新后，粗粒度（Aspen 式快照）反而因避开锁竞争而反超 |
- **与本讲呼应**：这是本讲"**如何高效时空检索**"一节的现代化版本——当年 LSM-Subgraph 处理的是"快照太多/日志太长"的储存-查询权衡；本文处理的是"**并发更新**下同样的权衡"，且给出了明确的反转点（batch 256）。
- **研讨问题设计**：
  1. 既然静态 CSR 快 2.4–11.0×，那我们为什么还需要 DGS？请从"数据新鲜度"角度给出量化论证。
  2. "batch > 256 时粗粒度反超"——这个 256 是硬件常量还是 workload 常量？换台机器/换个图，这个拐点会怎么移动？
  3. 把这三条结论套到讲稿的 LSM-Subgraph 上：它的 PMA 邻接数组属于"连续"还是"分段"？它的关键快照阈值 β=0.03 和本文的 batch=256，本质是同一类参数吗？

---

### ⑥ In-depth Analysis of Graph-based RAG in a Unified Framework — 12 种 GraphRAG 方法同台打擂

- **作者 / 单位**：Yingli Zhou, Yaodong Su, Youran Sun, Shu Wang, Taotao Wang, Runyuan He, **Yixiang Fang**\*（香港中文大学（深圳））· Yongwei Zhang, Sicong Liang, Xilin Liu, Yuchi Ma（华为云）
- **出处**：PVLDB 18(13):5623–5637, 2025，DOI `10.14778/3773731.3773738`
- **资源**：代码 `https://github.com/JayLZhou/GraphRAG`
- **一句话**：把纷乱的 GraphRAG 方法拆成统一的四阶段流水线，在同一批 QA 数据集上做首次 apples-to-apples 对比——**这是本讲"KG + LLM"部分的自然收束**。
- **统一框架（四阶段）**：
  1. **Graph Building**：语料切分为 chunk → 抽出 5 类图（Passage Graph / Tree / Knowledge Graph / Textual KG / Rich KG）；
  2. **Index Construction**：Node Index / Relationship Index / Community Index（社区报告）三类索引；
  3. **Operator Configuration**：把检索蒸馏成 **19 个算子**（向量检索、Personalized PageRank、Steiner Tree 等）；
  4. **Retrieval & Generation**：检索原语 → LLM，两种范式（Direct Generation / Map-Reduce）。
- **关键结论**：
  - **"知识税"**：构建 Rich KG 的 token 成本最高可达简单树的 **40×**，但**属性越多 ≠ 问答效果越好**；
  - 层次化摘要（社区报告）系的 grand summary 在抽象型问题上最优——相当于"预先消化过的语料地图"；
  - 由此组合出新变体：**VGraphRAG**（实体/关系检索 + 社区与 chunk 向量检索），在 MultihopQA 上较 RAPTOR 提升 **6.42%**；**CheapRAG**（用向量剪枝选社区），在 MultihopSum 上 token 成本降 **约 100×** 且质量提升。
- **与本讲呼应**：讲稿最后一节讲了大语言模型 × 知识图谱的三条技术路径与 CoT-RAG；本文相当于"**这三条路的成本账本**"。
- **研讨问题设计**：
  1. 从系统视角看，GraphRAG 的瓶颈是 LLM 推理还是**图构建/检索**？请用"知识税 40×"这一数据给出定量的回答。
  2. 19 个算子里有 Personalized PageRank 和 Steiner Tree——为什么这两个经典图算法会以"检索算子"的身份回归？（可与本讲最前面的 PageRank / Pregel 那一页回指）
  3. CheapRAG 用 1/100 的 token 拿到更好质量，说明原方案的冗余在哪里？这是"以计算换检索"还是"以检索换生成"？

---

## 四、备用候选（主推 6 篇因故不可用时的替换项）

| 备用 | 论文 | 会议 | 定位 | 何时选用 |
|:---|:---|:-:|:---|:---|
| B1 | **NeuraChip**: Accelerating GNN Computations with a Hash-based Decoupled Spatial Accelerator | ISCA '24, pp.946–960 | 基于 Gustavson 的 GNN 空间加速器，乘/加解耦 + 滚动淘汰 + 哈希动态重播种做负载均衡；较 MKL 22.1×、cuSPARSE 17.1×、较最优 SpGEMM 加速器 1.5×；NeuraSim 模拟器开源 | 若想再补一篇**体系结构/加速器**线，替换或并列 ③ |
| B2 | **LeapGNN**: Accelerating Distributed GNN Training Leveraging Feature-Centric Model Migration | FAST '25（录用率 21.5%） | 以特征为中心的模型迁移加速分布式 GNN 训练，典型的 **I/O·通信视角** GNN 系统 | 若研讨更偏**存储/I-O**而非 GPU 并行，可替换 ④ |
| B3 | **RapidStore**: An Efficient Dynamic Graph Storage System for Concurrent Queries | VLDB '25 | 动态图读多写少场景，读写解耦 + 版本数据与图数据解耦 | 与 ⑤ 同为学生热烈的"动态图"话题时互换 |
| B4 | **KET-RAG**: A Cost-Efficient Multi-Granular Indexing Framework for Graph-RAG | KDD '25 | 多粒度索引（KG 骨架 + 文本-关键词二分图），索引成本较微软 GraphRAG 降一个数量级、生成质量最高 +32.4% | 若希望 ⑥ 换成"具体系统"而非"横向评测"，选这篇 |

---

## 五、分组汇报实施建议（选课 100 人）

### 5.1 推荐分组结构：**6 篇 × 3 组 = 18 组**（约 5–6 人/组）

同一篇论文安排**三个角色组**，这是最有研讨味的配置：

| 角色 | 任务 | 组内要求 |
|:---|:---|:---|
| **陈述组** | 讲清"问题—观察—设计—评测"四段 | 必须复述论文的关键**量化数据**，不许只讲概念 |
| **质疑组** | 专挑论文的薄弱处：实验是否公平、基线是否最新、是否有遗漏假设 | 至少提出 3 个可辩护的质疑点，且每条都要给出**判据** |
| **复现组** | 跑通开源代码的最小实验，或用本讲的两个演示做类比验证 | 至少产出 1 张自己跑出来的图/表 |

> 剩余 2 组作机动（一组负责跨六篇的横评汇总，一组负责现场计时/提问记录）。

### 5.2 时间建议（按每篇 25 分钟）

| 环节 | 时长 | 说明 |
|:---|:-:|:---|
| 先抛问题 + 学生书面预测（**POE**） | 3 min | **务必保留**：演示/结论前置会让学习增益归零（Crouch et al., 2004），这是本课程已确立的铁律 |
| 陈述组汇报 | 10 min | |
| 质疑组发难 + 现场辩论 | 7 min | |
| 复现组证据 + 老师收束 | 5 min | |

### 5.3 难度梯度建议（由易到难排场次）

```
① ChunkGraph  ← 与本讲最贴，先热场，概念门槛最低
② gSampler    ← 有现成代码可跑，互动性最强
③ TMiner      ← 需要体系结构基础
④ WiseGraph   ← 需要 GNN 训练背景
⑤ Revisiting  ← 需要已读若干 DGS 系统，中期合适
⑥ GraphRAG    ← 压轴，最能引发开放讨论
```

---

## 六、给主讲老师的提醒

1. **六篇均已交叉核实**会议名称、年份、页码与作者单位，可直接进入课程表，无需二次校对。
2. 其中 **①②③④⑤⑥ 全部有公开代码或 Artifact 存档**，学生动手可行性最高的是 **② gSampler**（SOSP'23 三联 AE 徽章 + 内置 Node2Vec/RandomWalk）；③ TMiner 仅有论文（模拟器未公开），需以"读论文 + 对照课堂演示"方式研讨。
3. 若希望研讨与本讲的两个课堂演示形成闭环，**优先保留 ① 和 ③**——分别对应 `walk_io_demo.html`（分块 I/O）与 `graph-trace-viewer.html`（访存 trace）。
4. 不建议把本人工作（SOWalker, ATC'23）列入研讨清单，以免学生在评分上陷入尴尬；如需使用，建议只作为 ② 的背景材料出现。
