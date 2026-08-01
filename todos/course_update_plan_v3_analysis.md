# 《课程更新方案 v3》全面分析与落地编辑计划

> 分析对象：`todos/course_update_plan_v3.md`
> 分析日期：2026-08-01
> 落地窗口：两周（2026-08-01 ~ 2026-08-14），面向 2026 秋季学期

---

## 一、方案概述

### 1.1 方案结构拆解

v3 方案覆盖两门课，共 **6 项独立改进措施**，可归纳为下表：

| 编号 | 课程 | 改进措施 | 交付形态 | 依赖素材 |
|---|---|---|---|---|
| **M1** | 数据中心技术 | `data-center-intro.md` 前沿内容年度更新 | MARP 增量修订 | `d:\data\documents\collection\`（7769 文件，2026 年新增约 996） |
| **M2** | 数据中心技术 | 新建后备讲座《性能预测技术与服务质量保障》 | 全新 MARP（对标 `object-storage.md`） | `qos-guarantee.md` 骨架 + `research\publications\` |
| **M3** | 数据中心技术 | 新建后备讲座《智能运维技术与根因分析》 | 全新 MARP | `data-center-technology\aiops\` |
| **M4** | 数据中心技术 | 对象存储实验重构（MinIO → RustFS/VaultS3） | 实验教程 + 演示脚本 | `iot-storage-experiment\obs-tutorial\` |
| **M5** | 数据中心技术 | 智能运维实验设计（1 小时演示 + 课后作业） | 演示脚本 + 作业说明 | `aiops\experiment-course-2026.md` 等 |
| **M6** | 数据中心技术 | 卡片机集群教学环境评估与实验设计 | 环境可行性结论 + 实验方案 | `course-repository\bpidc-tutorial\` |
| **M7** | 计算机系统设计 | 《二阶随机游走技术与应用》讲座重构 | `system-for-graph.md` 重构 + 作业 | 已有骨架 + `research\publications\` |

### 1.2 教学设计意图

方案的核心意图是把《数据中心技术》从"**教师串讲 + 论文研讨**"升级为"**4 讲座 × 4 演示 × 1 作业**"的模块化结构，每讲形成"理论 → 现场演示 → 动手作业"的闭环。这在教学法上属于典型的 **研究引导型教学（research-led teaching）+ 交互式课堂演示（Interactive Lecture Demonstrations, ILD）** 组合，同时以卡片机集群提供实体化的"临场感"。

《计算机系统设计》则是把散点式的图系统讲稿，收敛到"二阶随机游走"这一条主线上，采用 **2 课时讲座 + 1 课时演示 + 1 课时作业分析** 的 4 课时切分。

### 1.3 现有素材成熟度速览

| 素材 | 规模 | 成熟度 | 判断 |
|---|---|---|---|
| `data-center-intro.md` | 2549 行 | ★★★★☆ | 结构完整，缺 2026 年新增前沿 |
| `object-storage.md` | 1882 行 | ★★★★★ | 风格标杆（三挑战结构） |
| `qos-guarantee.md` | 555 行 | ★★☆☆☆ | 骨架在，三大方法均为占位图，"我们的工作"停在 2019 前 |
| `system-for-graph.md` | 1381 行 | ★★★☆☆ | 995-1122 行已有随机游走节，约六成骨架 |
| `aiops\` 目录 | 多文件 | ★★☆☆☆ | 时序异常检测完整可跑，**根因分析零基础** |
| `obs-tutorial\` | 完整教程 | ★★★☆☆ | 结构好，但 MinIO 已不可用 |
| `bpidc-tutorial\` | 2 份清单 | ★★☆☆☆ | 硬件清单清晰，但架构受限严重 |

---

## 二、优势分析

### 2.1 「4 讲座 + 4 演示 + 1 作业」结构本身站得住

**优势一：演示环节把"看"变成"预测—观察—解释"的机会。**
方案给每讲配一个课堂演示，这不是装饰。物理教育研究里有一条被反复验证的结论：**被动观看演示对学习几乎无增益，但在演示前要求学生写下预测，增益显著**（Crouch et al., 2004）。方案中"性能指标预测实验演示""根因分析实验演示"天然适合 POE（Predict-Observe-Explain）：让学生先猜"加大并发后 P99 尾延迟会怎么变""注入故障后哪个指标先异常"，再跑演示。这是当前方案最大的、但**尚未被显式写出来**的潜力点。

**优势二：以研促教路径清晰，且素材真实存在。**
Healey (2005) 的研究—教学关系四象限中，方案同时踩到了三格：
- *research-led*（讲授研究成果内容）：HuGE/HuGE+/SOWalker/Graph3PO 直接进讲稿；
- *research-oriented*（讲授研究过程与方法）：尾延迟测量、根因定位方法论；
- *research-based*（学生做类研究的探究活动）：实验作业刷榜。

素材盘点确认这些论文是真实产出，不是硬凑：`HuGE (ICDE'21)`、`HuGE+ (IEEE TBD'23)`、`DistGER-Pipe (IEEE TKDE'25)`、`SOWalker (USENIX ATC'23)`、`Graph3PO (SC'23)`、`STGraph3PO (ACM TACO'26)`、`SPFaaS (IEEE TPDS'25)`、`KGQW (IEEE TPDS'26)`、`CoFS (IEEE TCAD'24)`。素材密度足以支撑两讲。

**优势三：后备讲座是正确的风险管理。**
三位合作老师各占一周，任何一位变动都会开天窗。准备两讲后备（M2/M3）覆盖了 2/3 的风险敞口，且这两讲本身可以在合作老师正常到场时转为"选讲/加餐"，不浪费。这是低成本高回报的安排。

**优势四：卡片机集群解决"云平台绑定厂商"的真实痛点。**
把集群搬上讲台的价值在教育文献中有支撑：Gooch et al. (2022) 基于 484 名学生的调查报告，物理 Raspberry Pi 集群在并行分布式计算（PDC）教学中能有效建立"分布式是真实的机器在协作"这一直觉；Shoop et al. (2025, JPDC) 报告了多年使用 Pi 集群教 PDC 的正面评估。方案的三条理由（讲台契合、临场感、避免厂商绑定）与文献结论一致。

**优势五：《计算机系统设计》的 2+1+1 切分是合理的时间预算。**
2 课时讲座（约 90 分钟）讲清 node2vec 的二阶游走定义 + I/O 挑战 + SOWalker 方案，1 课时演示，1 课时作业分析。相比"4 课时全讲"，留出的演示与作业分析时间正是把 research-led 推向 research-based 的关键。

### 2.2 已有素材的复用率高

- `object-storage.md` 的"挑战一扩展 / 挑战二长尾 / 挑战三预测"三段式，是可直接套用到 M2、M3 的模板，风格统一成本低。
- `system-for-graph.md` 第 995-1122 行的"表示学习与随机游走"节已含 HuGE+/SOWalker 图表，重构不是从零开始。
- `obs-tutorial` 的"实验一搭建 / 实验二性能观测 / 实验三尾延迟挑战"三段设计与 `object-storage.md` 讲稿的三挑战结构天然对齐，只需换掉软件栈。
- `aiops\classroom-warmup\` 基于 sklearn，2 分钟跑完，是最成熟的现成演示素材。

---

## 三、潜在问题

按严重程度排序。前三项属于**会导致方案在开学时无法交付**的级别。

### 🔴 P0-1：智能运维讲座的主题与已有准备严重错配

方案 M3/M5 写的是"**智能运维技术与根因分析**"，但对 `aiops\` 目录的排查结论是：

- `experiment-course-2026.md`：完整可执行，2 课时演示 + 3 周刷榜，基于 EasyTSAD，评分指标 PointF1PA / EventF1PA 定义明确——但**100% 是时序异常检测（TSAD）**；
- `Results/` 下仅有 LOF / SubLOF × AIOPS 的跑分结果，同属异常检测；
- `classroom-warmup/`：sklearn 异常检测，成熟但仍是异常检测；
- **根因分析（RCA）：零代码、零数据集、零演示脚本**；
- `platform-research-2026.md`：纯纸面调研，无落地。

也就是说，讲座标题承诺的"根因分析"是当前**准备度最低**的部分，而准备最充分的"异常检测"没有出现在标题里。两周内从零搭 RCA 演示（需要 trace 数据、服务依赖图、因果推断或图算法实现）风险极高。

**建议处置**：调整讲座定名为"**智能运维技术：从异常检测到根因分析**"，把已成熟的 TSAD 作为演示与作业主体（占 70%），RCA 作为方法论讲解 + 一个轻量 case（占 30%，用 `aiops_cn_analysis.md` 里的 Trace 根因定位建议做纸面推演，不强求可跑代码）。这样标题诚实、内容可交付。

### 🔴 P0-2：RustFS 不支持 32 位 ARM，与卡片机集群直接冲突

技术核查结果：

| 方案 | 许可 | 状态 | armv7/armhf | arm64 | 结论 |
|---|---|---|---|---|---|
| MinIO | AGPLv3 | **维护模式**；2025-05 移除 Web UI 管理功能，停止社区版二进制分发 | 历史版本有 | 有 | 不宜作为新教程主线 |
| **RustFS** | Apache 2.0 | **全 beta**（1.0.0-beta.12） | ❌ **无构建** | ✅ | 仅支持 x86_64 / aarch64 / macos-arm64 / windows-x86_64 |
| SeaweedFS | Apache 2.0 | 稳定 | ✅ linux_arm | ✅ | 卡片机可行 |
| Garage | AGPLv3 | 稳定 | ✅ | ✅ | 轻量，可选 |
| Ceph RGW | LGPL | 稳定 | 资源要求高 | ✅ | 卡片机不可行 |

而卡片机集群的实际配置是：
- **BPI-M3 × 8**：`armv7l` **32 位**，2GB/节点，千兆网；
- **RPi 1 B+ × 4**：`armv6l`，512MB，100Mbps，且**无免密 sudo**。

结论：**M4（换 RustFS）与 M6（卡片机集群）在当前硬件上无法同时成立**。而且 RustFS 全版本仍是 beta，作为教学环境有稳定性风险；VaultS3 未见广泛使用与文档，不建议作为主线。

**建议处置**：
- **讲台演示（M6，卡片机）**：改用 **SeaweedFS**，官方提供 `linux_arm` 构建，内存占用低，适配 BPI-M3。RPi 1 B+ 集群（armv6l/512MB/百兆）仅作为"极限环境演示"或备份，不承担主线。
- **交作业环境（M4）**：既然方案明确"交作业就不用这个（卡片机）"，作业环境可用 x86_64，此时 **RustFS 可用**，但建议 **SeaweedFS 为主 + RustFS 为对照**，避免把整门实验押在 beta 软件上。
- 若坚持单一软件栈以降低学生认知负担，**SeaweedFS 是唯一能同时覆盖讲台 armv7 与作业 x86_64 的选项**。

### 🔴 P0-3：两周工期与 6 项交付物之间存在缺口

M2、M3 各需要一份对标 `object-storage.md`（1882 行）的完整 MARP。`qos-guarantee.md` 只有 555 行且三大方法（控制论 / 约束优化 / 机器学习）全是占位图，等于要新写约 1300 行；M3 更是要从零组织。加上 M4 实验重构、M6 环境评估、M7 讲稿重构，两周（按每天 4 小时有效工作计约 56 小时）非常紧。

**建议处置**：按"**开学前必须完成 / 开学后滚动完成**"两档切分（见第五节排期）。M1、M7 必须在开学前完成（第 10 周、系统设计课要用）；M2、M3 作为后备讲座，实际使用时间在第 12-14 周，可以延后到 9 月中旬完成，只需在两周内完成**骨架 + 素材归位**。

### 🟠 P1-1：「二阶随机游走」命名与素材主体存在定位断层

- `HuGE (ICDE'21)` / `HuGE+ (IEEE TBD'23)` / `DistGER-Pipe (TKDE'25)` 的核心是**信息熵驱动的有偏一阶游走**（heterogeneous graph embedding 的游走策略优化），严格来说不是二阶；
- **真正的二阶随机游走系统是 `SOWalker (USENIX ATC'23)`**（out-of-core 二阶游走）；
- 外部经典文献 `node2vec (KDD'16)` 才是二阶游走的定义源头，`GraSorw (VLDB'22)` 是另一个 out-of-core 二阶游走系统。

如果讲座定名"二阶随机游走技术与应用"，却用 HuGE 系列占主体，学生会困惑于"这到底二阶在哪"。

**建议处置**：讲座主线按"**一阶 → 有偏一阶 → 二阶**"递进组织：
1. DeepWalk (KDD'14) 一阶游走 + Skip-gram（10 分钟）
2. node2vec (KDD'16) p/q 参数与二阶转移概率的**形式化定义**（15 分钟，这是核心概念）
3. 二阶游走的系统挑战：状态空间从 O(|V|) 涨到 O(|E|)、随机 I/O 放大（10 分钟）
4. 系统方案：KnightKing (ATC'19) 内存式 → GraSorw (VLDB'22) / **SOWalker (ATC'23)** out-of-core（25 分钟，SOWalker 为重点）
5. 有偏游走的另一条路：**HuGE/HuGE+ 的熵驱动**（15 分钟，定位为"游走质量优化"而非二阶）
6. 分布式扩展：DistGER-Pipe (TKDE'25)（10 分钟）

需补充的外部文献讲解约 20-25 分钟，正好填满 2 课时中已有六成骨架之外的空缺。

### 🟠 P1-2：1 小时演示的时间预算普遍偏乐观

- `aiops\experiment-course-2026.md` 原设计是 **2 课时演示**，方案压缩到 1 小时，EasyTSAD 环境配置 + 数据加载 + 多算法对比 + 评分解读，60 分钟大概率超时；
- `classroom-warmup/` 虽然 2 分钟跑完，但"按 90 分钟编排需压时"的结论说明它内容量偏小，需扩充；
- 对象存储实验的"搭建 + 性能观测 + 尾延迟"三段，在 60 分钟内做完三段几乎不可能。

**建议处置**：统一采用"**预置环境 + 分段演示**"原则——
- 所有环境（容器镜像 / conda 环境 / 集群服务）**课前预装并冷启动完成**，课堂上不做安装；
- 每个 60 分钟演示切成 3 段 × 15 分钟 + 3 次 5 分钟 POE 预测/讨论；
- 耗时步骤（大数据集跑分、长时间压测）**准备好预生成结果**，现场只跑小规模验证 + 展示预生成结果。

### 🟠 P1-3：卡片机集群"机器在办公室、暂时不能直接访问"带来验证盲区

方案自述无法直接访问硬件。这意味着 M6 的所有设计目前都是纸面推演。BPI-M3 的 armv7l + 2GB 内存在跑 SeaweedFS 多节点 + 客户端压测时，内存与网络是否够用，**必须实测**。RPi 1 B+ 的 armv6l 更是许多现代 Go 二进制不再提供构建的架构。

**建议处置**：把"**取得硬件访问 + 完成 SeaweedFS armv7 冒烟测试**"列为两周内的**硬性里程碑**，且设置决策点：若 8 月 8 日前未完成实测，M6 降级为"课堂展示实物 + 播放录屏"，不做现场交互式演示。

### 🟡 P2-1：`data-center-intro.md` 前沿更新的素材命中不均

对 `d:\data\documents\collection\`（7769 文件）的排查结论：

**强命中（可直接成节）**：
| 主题 | 文摘数 | 现有讲稿覆盖 |
|---|---|---|
| 超节点 / Scale-up | 18 | **0**（完全缺失） |
| 国产算力 / 昇腾 | 30 | **0** |
| KV Cache | 16 | 1 |
| 算力泡沫 / 投资周期 | 11 | 0 |
| CXL | 7 | 1 |
| 电力约束 / 核电 | 5 | 核电 0 |

**零命中（需沿用旧索引 `related-material-data-center-2026.md`）**：东数西算、对象存储、AIOps、绿色数据中心。

现有讲稿中 PUE 出现 38 处、液冷 11 处、东数西算 4 处，基础扎实；缺口集中在**架构层（超节点/CXL）**、**产业层（国产算力/算力泡沫）**、**能源层（核电/电力约束）**。

**建议处置**：新增 3 节，不要平铺 132 篇文摘，每节控制在 8-12 张片。

### 🟡 P2-2：作业排行榜机制的公平性与工作量需明确

方案提到实验作业（含"备用"标记）。`experiment-course-2026.md` 的 3 周刷榜设计（EasyTSAD + PointF1PA/EventF1PA）本身是好的 research-based 实践，但要注意：
- 排行榜易诱发"调参军备竞赛"，与"理解方法"的教学目标偏离；
- 需明确成绩构成中排名占比（建议 ≤ 30%），其余给**方法报告与复现性**；
- 需设 baseline 分数线，保证认真做的学生不会因排名靠后而挂科。

### 🟡 P2-3：`qos-guarantee.md` 的"我们的工作"时间线断层

现有内容停在 PSLO (EuroSys'16) 等 2019 年前的 PI 控制器工作，与讲座要展示的"研究前沿"形象不符。而 `Graph3PO (SC'23)`、`STGraph3PO (ACM TACO'26)`、`SPFaaS (IEEE TPDS'25)` 正好可以填补"机器学习方法"占位图和 2016→2026 的演进线。

### 🟡 P2-4：杂项清理

- `aiops/` 根目录 `TSADEval.log` 为早期失败运行残留，建议删除；
- `obs-tutorial` 中所有 MinIO Web UI 相关截图与操作步骤已失效（2025-05 已移除该功能），必须整段删除而非修补。

---

## 四、文献支撑

### 4.1 课堂演示的有效性：预测是关键，被动观看无效

**Crouch, C., Fagen, A. P., Callan, J. P., & Mazur, E. (2004). "Classroom demonstrations: Learning tools or entertainment?" *American Journal of Physics*, 72(6), 835-838.**

哈佛的对照实验，结论极其明确：**仅观看演示的学生，其理解水平与完全没看演示的学生无显著差异**；而在演示前被要求**写下预测**的学生，理解水平显著提升；进一步讨论演示结果的学生提升最大。

> 对本方案的意义：M1/M4/M5/M7 的四个演示如果只是"老师在台上跑一遍，学生在下面看"，教学收益接近于零。**必须在每个演示前插入 2-3 分钟的书面预测环节**，这是零成本但决定演示成败的设计。

**Sokoloff, D. R., & Thornton, R. K. (1997). "Using Interactive Lecture Demonstrations to Create an Active Learning Environment." *The Physics Teacher*, 35(6), 340-347.**

提出 Interactive Lecture Demonstrations (ILD) 的标准八步流程：描述演示 → 学生独立填写预测表 → 小组讨论 → 记录最终预测 → 执行演示 → 学生描述观察结果 → 讨论与解释 → 推广到类似情境。使用 ILD 的班级在概念测试上的 **normalized gain 达 30%-90%**，远高于传统讲授的约 20%。

> 对本方案的意义：ILD 八步是可以直接搬用的演示脚本模板。建议把每个 60 分钟演示按"3 × (预测 5min + 演示 10min + 解释 5min)"编排。

### 4.2 以研促教：Healey 的研究—教学关系四象限

**Healey, M. (2005). "Linking research and teaching to benefit student learning." *Journal of Geography in Higher Education*, 29(2), 183-201.**

按两个维度（学生是听众 vs 参与者；强调研究内容 vs 研究过程）划分四象限：

| | 强调研究**内容** | 强调研究**过程与问题** |
|---|---|---|
| **学生作为参与者** | research-tutored（研讨会讨论研究论文） | **research-based**（学生自己做探究） |
| **学生作为听众** | **research-led**（讲授前沿研究成果） | research-oriented（讲授研究方法论） |

Healey 明确指出：**单纯的 research-led 对学生学习的正向影响最弱**；把学生推向 research-based 才是研究型大学的核心竞争力。

> 对本方案的意义：v3 方案的四讲天然处于 research-led 象限（讲自己的论文）。真正的增值来自配套的演示（research-oriented，展示方法）与作业（research-based，学生自己做）。因此**实验作业不应被标为"备用"**——它恰恰是教学收益最大的部分。建议把对象存储与性能预测的作业至少保留一份为必做。

### 4.3 物理集群教 PDC：有效，但有明确的两大挑战

**Gooch, D., et al. (2022). "Passive or active learning? Investigating the use of Raspberry Pi clusters in distributed computing education." *Open Learning: The Journal of Open, Distance and e-Learning*.**

基于 **484 名学生**的调查。正面结论：物理集群显著提升学生对分布式系统的具象理解与学习动机。但报告了两大挑战：
1. **支持学生主导的编程式主动学习困难**——学生容易停留在"跟着敲命令"的被动状态；
2. **远程支持低分学生困难**——硬件故障、环境差异会让基础薄弱的学生卡死。

**Shoop, E., et al. (2025). "Teaching parallel and distributed computing with Raspberry Pi clusters." *Journal of Parallel and Distributed Computing*.**

多年期评估，正面报告 Pi 集群在 PDC 课程中的教学效果，同时强调**预置镜像与自动化部署脚本**是降低运维负担的关键。

> 对本方案的意义：M6 的三条理由与文献一致，但要正视两大挑战。具体到本方案：
> - 挑战 1 的对策：卡片机集群只做**讲台演示**（方案已明确"交作业就不用这个"），这实际上规避了让学生自己操作硬件的坑，是正确决策；
> - 挑战 2 的对策：作业环境用 x86_64 + 预置容器镜像，保证低分学生不被环境问题淘汰；
> - Shoop 的"预置镜像"建议直接对应本方案的 P1-2 处置（课前预装、不在课堂上做安装）。

### 4.4 认知负荷：为什么 1 小时演示必须分段

**Sweller, J., van Merriënboer, J., & Paas, F. (1998/2019). "Cognitive Architecture and Instructional Design." *Educational Psychology Review*.**

工作记忆容量有限，连续高密度信息输入会导致 extraneous cognitive load 溢出。分段呈现（segmenting principle）与暂停反思是标准对策。

**Mayer, R. E. (2009). *Multimedia Learning* (2nd ed.). Cambridge University Press.** — Segmenting Principle：学习者自控节奏的分段呈现优于连续呈现。

> 对本方案的意义：直接支持 P1-2 的"3 段 × 15 分钟 + 3 次 POE"编排。

### 4.5 竞赛式作业：有效但需防偏

**Lawrence, R. (2004). "Teaching data structures using competitive games." *IEEE Transactions on Education*, 47(4), 459-466.** — 竞赛机制显著提升参与度与投入时间。

**Kaggle-in-Class 与教学实践的普遍经验**：排行榜提升动机，但需配套"方法报告"评分项以防止纯调参。

> 对本方案的意义：支持 P2-2 的建议——排名占比 ≤ 30%，其余给方法报告与可复现性。

### 4.6 技术选型的事实依据（非教育文献，但同等重要）

| 事实 | 来源与核查 |
|---|---|
| MinIO 于 2025-05 从社区版移除 Web UI 管理功能，停止社区版二进制分发，项目进入维护模式 | MinIO 官方 release notes 与社区讨论 |
| RustFS 当前最新为 1.0.0-beta.12，**全部版本为 beta**；发布构建仅含 x86_64-linux / aarch64-linux / macos-arm64 / windows-x86_64，**无 armv7/armhf** | RustFS GitHub Releases API 核查 |
| SeaweedFS 官方发布包含 `linux_arm`（32 位）与 `linux_arm64` 构建 | SeaweedFS GitHub Releases |
| BPI-M3 为 `armv7l` 32 位，2GB/节点；RPi 1 B+ 为 `armv6l`，512MB，百兆网，无免密 sudo | `bpidc-tutorial/cluster-inventory.md` 与 `cluster-inventory-rpi1b.md` |

---

## 五、工作区编辑计划

### 5.1 优先级与决策点

```
必做（开学前，第 10-11 周要用）
  ├─ M1  data-center-intro.md 前沿更新     ← 第 10 周讲
  ├─ M7  system-for-graph.md 二阶游走重构  ← 系统设计课
  └─ M4  对象存储实验重构（软件栈切换）    ← 第 11 周演示

滚动（9 月中旬前完成即可，第 12-14 周才可能用）
  ├─ M2  qos-guarantee.md → 完整后备讲座
  ├─ M3  aiops 后备讲座
  └─ M5  智能运维实验设计

带决策点
  └─ M6  卡片机集群  → 8/8 决策：能实测则做现场演示，否则降级录屏
```

### 5.2 逐文件编辑清单

#### 【M1】`data-center-intro.md`（修改，+约 30 片）

在现有"集中运维挑战"之前插入 3 个新节：

| 新增节 | 插入位置 | 片数 | 素材来源 |
|---|---|---|---|
| **超节点与 Scale-up 架构** | "基础硬件"节之后 | 10-12 | collection 中 18 篇超节点/Scale-up 文摘 + 现有 CXL 1 处扩写 |
| **算力经济学：泡沫、周期与国产替代** | "集中使用成本(TCO)"节之后 | 8-10 | 30 篇国产算力 + 11 篇算力泡沫 |
| **电力约束与新型能源供给** | "集中供能效率(PUE)"节之后 | 8-10 | 5 篇电力约束 + 核电（现 0 处）+ 已有液冷 11 处衔接 |

同时对已有内容做小幅更新：
- "平台软件与负载"节补 **KV Cache 与推理负载特征**（collection 有 16 篇，现讲稿仅 1 处）；
- "国家算力网"节的东数西算数据更新到 2026（collection 零命中，沿用 `todos/related-material-data-center-2026.md` 旧索引）。

**执行方式**：先从 `related-material-data-center-2026.md` 与 collection 中筛出每个主题 top-10 文摘 → 提炼 3-5 个核心论点 → 每论点 2-3 片（论点 + 数据图表 + 案例）。

#### 【M7】`system-for-graph.md`（重构，第 995-1122 行为基础）

按 P1-1 的六段递进结构重写：

| 段 | 内容 | 时长 | 素材状态 |
|---|---|---|---|
| 1 | DeepWalk (KDD'14) 一阶游走 + Skip-gram | 10 min | **需新增**（外部文献） |
| 2 | node2vec (KDD'16) p/q 与二阶转移概率形式化 | 15 min | **需新增**（外部文献，本讲核心概念） |
| 3 | 二阶游走的系统挑战：状态空间 O(\|E\|)、随机 I/O 放大 | 10 min | **需新增** |
| 4 | KnightKing (ATC'19) → GraSorw (VLDB'22) → **SOWalker (ATC'23)** | 25 min | SOWalker 已有图表，KnightKing/GraSorw **需新增** |
| 5 | 熵驱动有偏游走：HuGE (ICDE'21) / HuGE+ (TBD'23) | 15 min | **已有**，需重新定位为"游走质量优化" |
| 6 | 分布式扩展：DistGER-Pipe (TKDE'25) | 10 min | **已有** |

**课堂演示（1 课时）设计建议**：
在小图（如 Zachary Karate Club / Cora）上，用 node2vec 参数 p、q 做**可视化对比实验**——
- POE 环节：先让学生预测"p 大 q 小"和"p 小 q 大"分别会产生 BFS 式还是 DFS 式游走，嵌入可视化会呈现同质性（homophily）还是结构等价性（structural equivalence）；
- 演示：现场跑 `node2vec` + t-SNE 降维，2 分钟出图；
- 解释：对照预测，讲清 p/q 的语义。
这个演示轻量（笔记本可跑）、视觉冲击强、直接对应讲座核心概念，比跑大规模系统更适合课堂。

**实验作业（1 课时布置）**：
现有第 1321-1382 行的天池知识图谱链接预测赛可保留为选项，但建议改为**更贴合二阶游走的题目**：给定中等规模图，要求学生实现 out-of-core 的二阶游走采样器（或基于给定框架优化 I/O），以**采样吞吐 + 嵌入质量（链接预测 AUC）**双指标评分。排名占比 ≤ 30%。

#### 【M4】对象存储实验重构（新建目录）

在 `cs-courses` 工作区外的实验仓库中新建，或在 `d:\data\documents\portfolio\Course\data-center-technology\` 下建 `obs-tutorial-2026\`：

| 文件 | 动作 | 说明 |
|---|---|---|
| `README.zh_cn.md` | 基于旧版重写 | **删除所有 MinIO Web UI 相关章节与截图**（功能已移除） |
| `lab1-deploy.md` | 重写 | SeaweedFS 单机 → 多节点部署（x86_64 作业环境） |
| `lab2-perf.md` | 保留结构，换工具 | warp / s3bench 压测，观测吞吐与延迟分布 |
| `lab3-taillatency.md` | 保留结构 | 尾延迟测量与 P99 分析，对接 `object-storage.md` 挑战二 |
| `appendix-rustfs.md` | **新增** | RustFS 作为对照实验（标注 beta 状态） |

**软件栈决策**：主线 SeaweedFS（Apache 2.0、稳定、armv7+x86_64 双覆盖），RustFS 作为附录对照，MinIO 仅在讲稿中作为"生态变迁案例"提及（这本身是很好的教学素材：开源许可与商业化的张力）。

#### 【M2】`qos-guarantee.md` → 完整后备讲座（扩写 555 → 约 1300 行）

对标 `object-storage.md` 三挑战结构重组：

| 现有内容 | 处置 |
|---|---|
| 背景 / SLA-SLO-SLI | 保留，压缩 |
| 过度供应 / 性能干扰 | 保留，作为"挑战一：干扰不可控" |
| 经典机制 cgroup/BFQ/mClock | 保留，扩充为完整一节 |
| MAPE 环 | 保留 |
| 三方法（控制论 / 约束优化 / 机器学习）**各仅占位图** | **重点补全**：控制论用 PSLO 展开；约束优化补；**机器学习方法用 Graph3PO (SC'23) / STGraph3PO (TACO'26) 填充** |
| "我们的工作"停在 2019 前 | **补 2016 → 2026 演进线**：PSLO (EuroSys'16) → Graph3PO (SC'23) → SPFaaS (TPDS'25) → STGraph3PO (TACO'26) |

**演示设计（1 小时）**：性能指标预测实验——给定历史负载 trace，现场对比"移动平均 / ARIMA / 轻量 ML 模型"的预测误差。POE：让学生预测哪种方法在突发负载下表现最好。

#### 【M3】智能运维后备讲座（新建 `aiops-rca.md`）

**关键调整：讲座定名改为《智能运维技术：从异常检测到根因分析》**

| 节 | 内容 | 占比 | 素材状态 |
|---|---|---|---|
| 1 | AIOps 全景与运维数据三支柱（Metrics/Logs/Traces） | 15% | `aiops_cn_analysis.md` 可用 |
| 2 | **时序异常检测**：算法谱系、评价指标陷阱（PointF1PA vs EventF1PA） | 40% | **成熟**，`experiment-course-2026.md` 直接可用 |
| 3 | 日志异常检测 | 15% | `aiops_cn_analysis.md` 有建议，需补 |
| 4 | **根因分析**：方法论（依赖图 + 因果推断 + 指标传播）、工业案例 | 25% | **需新建**，以方法论讲解 + 纸面 case 为主 |
| 5 | LLM 运维智能体展望 | 5% | `aiops_cn_analysis.md` 有建议 |

**为什么这样切**：这是在"标题诚实"与"两周可交付"之间的唯一现实解。RCA 用 25% 篇幅做方法论讲解是可行的（不需要可跑代码），而把 40% 给已经完全就绪的异常检测，保证演示与作业质量。

#### 【M5】智能运维实验设计（修改 `aiops\experiment-course-2026.md`）

| 调整项 | 原设计 | 新设计 |
|---|---|---|
| 演示时长 | 2 课时 | **1 课时（60 min）**：3 段 × 15 min + 3 次 5 min POE |
| 环境 | 现场配置 | **课前预置 conda 环境 + 数据集**，课堂零安装 |
| 大数据集跑分 | 现场跑 | **预生成结果**，现场只跑小规模验证 |
| 作业周期 | 3 周刷榜 | 保留 3 周 |
| 评分 | 排名为主 | **排名 ≤ 30% + 方法报告 40% + 可复现性 30%**，设 baseline 及格线 |

同时：
- 扩充 `classroom-warmup/`（当前 2 分钟跑完，内容量偏小），补 2-3 个对比算法与可视化；
- **删除 `aiops/` 根目录的 `TSADEval.log`**（早期失败运行残留）。

#### 【M6】卡片机集群（修改 `bpidc-tutorial\`）

**8 月 8 日决策点前必须完成**：
1. 取得办公室硬件访问；
2. 在 BPI-M3（armv7l）上完成 SeaweedFS `linux_arm` 构建的**冒烟测试**：单节点启动 → 3 节点组集群 → 写入/读取 1000 个小对象 → 记录内存占用与吞吐。

| 测试结果 | 处置 |
|---|---|
| ✅ 通过 | 新建 `bpidc-tutorial/lab-seaweedfs-arm.md`，设计"讲台上的 8 节点对象存储集群"现场演示：节点故障注入 → 观察数据可用性与延迟变化（POE：预测拔掉一个节点后会发生什么） |
| ❌ 失败 | M6 降级：课堂展示实物 + 播放预录屏幕录像；`cluster-inventory.md` 中标注架构限制结论，留作后续硬件升级依据 |

**无论结果如何**，都需在 `cluster-inventory.md` 中补一节"**软件栈兼容性矩阵**"，明确记录 RustFS 无 armv7 构建、SeaweedFS 支持 linux_arm 这一核查结论，避免后续重复踩坑。

#### 【M-common】跨文件的统一改造：为每个演示加 POE 环节

这是**成本最低、收益最高**的单项改动（Crouch 2004 的直接应用）。在四个演示脚本中各插入一页 MARP：

```markdown
## 动手前：先预测

<!-- 给学生 3 分钟，要求写在纸上，不要讨论 -->

1. 【预测题 1】...
2. 【预测题 2】...

> 写完后与同桌交换，再看演示结果
```

各演示的预测题建议：
- **数据中心负载演示**：负载从 CPU 密集切到 I/O 密集时，哪个指标先饱和？
- **对象存储演示**：并发从 10 提到 100，平均延迟与 P99 延迟哪个涨得更快？为什么？
- **性能预测演示**：突发负载下，移动平均与 ML 模型谁的误差更大？
- **根因分析/异常检测演示**：PointF1 与 EventF1 在这段 trace 上谁的分数更高？

### 5.3 两周排期

| 日期 | 任务 | 交付物 |
|---|---|---|
| 8/1 (六) | 取得卡片机访问 + collection 文摘按 3 主题筛选 | 素材清单 |
| 8/2-8/4 | **M1**：data-center-intro 三新节撰写 | +30 片 |
| 8/5-8/6 | **M7**：system-for-graph 二阶游走重构（段 1-4） | 讲稿主体 |
| 8/7 | **M7**：node2vec p/q 可视化演示脚本 + 作业设计 | 演示可跑 |
| **8/8** | **决策点**：BPI-M3 SeaweedFS 冒烟测试 | 通过/降级结论 |
| 8/9-8/11 | **M4**：obs-tutorial-2026 三个 lab 重写 | 实验教程 |
| 8/12 | **M5**：aiops 演示压缩到 60 min + 评分方案 | 修订稿 |
| 8/13 | **M6**：按决策结果落地（现场演示脚本 或 录屏） | 演示方案 |
| 8/14 | **M-common**：四个演示统一加 POE 页 + 全量复核 | 收尾 |
| 9 月上中旬（滚动） | **M2** qos-guarantee 扩写、**M3** aiops-rca 新建 | 两份后备讲座 |

### 5.4 落地检查清单

- [ ] `data-center-intro.md` 新增超节点、算力经济、电力约束三节
- [ ] `data-center-intro.md` 补 KV Cache 与推理负载
- [ ] `system-for-graph.md` 按一阶→有偏一阶→二阶重构
- [ ] node2vec p/q 可视化演示脚本可在笔记本 2 分钟内跑完
- [ ] 二阶游走实验作业题目与评分标准（排名 ≤ 30%）
- [ ] `obs-tutorial-2026/` 建立，MinIO Web UI 相关内容全部删除
- [ ] SeaweedFS 作为主线软件栈，RustFS 作为附录对照
- [ ] BPI-M3 SeaweedFS armv7 冒烟测试完成（8/8 前）
- [ ] `cluster-inventory.md` 补软件栈兼容性矩阵
- [ ] AIOps 讲座更名为"从异常检测到根因分析"
- [ ] AIOps 演示压缩至 60 分钟，环境课前预置
- [ ] `aiops/TSADEval.log` 删除
- [ ] 四个演示全部插入 POE 预测页
- [ ] 实验作业去掉"备用"标记，至少一份定为必做
- [ ] `qos-guarantee.md` 机器学习方法节用 Graph3PO/STGraph3PO 填充（9 月）
- [ ] `qos-guarantee.md` "我们的工作"补 2016→2026 演进线（9 月）

---

## 六、一句话总结

方案的教学结构（讲座—演示—作业闭环、以研促教、实体集群）在文献上完全站得住，**但有三处会卡在开学前**：AIOps 讲座标题承诺的"根因分析"零准备而"异常检测"已就绪（建议更名并按 40:25 配比）、RustFS 无 armv7 构建导致换栈与卡片机集群互斥（建议统一改用 SeaweedFS）、6 项交付物两周排不下（建议 M1/M4/M7 必做、M2/M3 滚动到 9 月）。此外，**给每个演示加 3 分钟书面预测环节**是本次改进中性价比最高的一项——Crouch et al. (2004) 的结论是，没有这一步，演示的学习增益接近于零。
