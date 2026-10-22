# 数据中心技术 · 论文研讨课选题清单（36 篇）

> **课程**：数据中心技术（军山课堂，专业硕士 80 人）
> **研讨周**：第 15 / 16 / 17 周，**12-11 / 12-18 / 12-25**（周五下午 4 节连堂，A2-B106）
> **选题时间**：2026 年 11 月上旬（以课堂通知为准）
> **分组规则**：每篇论文 1 组（2–3 人），36 篇共 36 组，覆盖全班 80 人
> **形式**：每篇 12 分钟报告 + 3 分钟对抗问答，同专题 6 篇分两区对抗（分区与配对上课前公布）

**论文获取**：以下标题均为会议录用标题（逐字核实），可直接在 USENIX / ACM / IEEE Xplore 或学校图书馆检索下载全文。

---

## 第 15 周 · 12-11

### Session 1 · 对象存储与元数据（第 1–2 节）

| # | 论文 | 会议 | 一句话方向 |
|:--:|---|:--:|---|
| 1 | Mantle: Efficient Hierarchical Metadata Management for Cloud Object Storage Services | SOSP'25 | 云对象存储的分层元数据管理 |
| 2 | ACOS: Apple's Geo-Distributed Object Store at Exabyte Scale | FAST'26 | Apple EB 级全球分布式对象存储系统 |
| 3 | Managing Scalable Direct Storage Accesses for GPUs with GoFS | SOSP'25 | 面向 GPU 的可扩展直接存储访问管理 |
| 4 | Rearchitecting the Thread Model of In-Memory Key-Value Stores with μTPS | SOSP'25 | 重构内存 KV 存储线程模型以降延迟 |
| 5 | Running Consistent Applications Closer to Users with Radical for Lower Latency | SOSP'25 | 把一致性应用部署到离用户更近处以降延迟 |
| 6 | "Range as a Key" is the Key! Fast and Compact Cloud Block Store Index with RASK | FAST'26 | 云块存储"以范围作键"的快速紧凑索引 |

### Session 2 · 固态存储与闪存管理（第 3–4 节）

| # | 论文 | 会议 | 一句话方向 |
|:--:|---|:--:|---|
| 7 | LOONG: Utilizing Long-Stride Reprogramming to Enhance the Performance of SSDs | ISCA'26 | SSD 长跨步重编程提升性能 |
| 8 | BoostX-NTI: Fast, Scalable and Flexible Storage Architecture with NVMe/TCP Initiator Acceleration | ISCA'26 | NVMe/TCP Initiator 加速的存储架构 |
| 9 | DPAS: A Prompt, Accurate and Safe I/O Completion Method for SSDs | FAST'26 | SSD 快速、准确、安全的 I/O 完成机制 |
| 10 | Aeolia: A Fast and Secure Userspace Interrupt-Based Storage Stack | SOSP'25 | 快速安全的用户态中断式存储栈 |
| 11 | Sleeping with One Eye Open: Fast, Sustainable Storage with Sandman | SOSP'25 | 兼顾速度与可持续（节能）的存储 |
| 12 | SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs | FAST'26 | 内存受限 PC 上的 SSD 加速 LLM 推理 |

---

## 第 16 周 · 12-18

### Session 3 · 内存层次与 CXL/HBM 互联（第 1–2 节）

| # | 论文 | 会议 | 一句话方向 |
|:--:|---|:--:|---|
| 13 | Vistara: Making CXL Real—Full Path from ASIC Design and OS Support to Hyperscale Deployment（Meta） | ISCA'26 | CXL 从 ASIC 设计、OS 支持到超大规模部署 |
| 14 | Oasis: Pooling PCIe Devices Over CXL to Boost Utilization | SOSP'25 | 通过 CXL 池化 PCIe 设备提升利用率 |
| 15 | HBM-CASO: A Coordinated Approach to HBM System-Level and On-Die ECC | ISCA'26 | HBM 系统级与片上 ECC 协同纠错 |
| 16 | Scalable Far Memory: Balancing Faults and Evictions | SOSP'25 | 远端内存中故障与逐出的平衡 |
| 17 | Five-Minute Rule 40 Years Later: A First-Principles Revisit for Modern Memory Hierarchy | ISCA'26 | "五分钟规则"40 年后的第一性原理重审 |
| 18 | Demeter: A Scalable and Elastic Tiered Memory Solution for Virtualized Cloud via Guest Delegation | SOSP'25 | 虚拟化云中的弹性分层内存（客户机委托） |

### Session 4 · 可靠性与故障检测/预测（第 3–4 节）

| # | 论文 | 会议 | 一句话方向 |
|:--:|---|:--:|---|
| 19 | ColumnKeeper: Efficient Solutions to the ColumnDisturb Vulnerability in DRAM-based Systems | ISCA'26 | DRAM 列干扰（ColumnDisturb）漏洞的高效防护 |
| 20 | PVAC: A RowHammer Mitigation Architecture Exploiting Per-victim-row Counting | ISCA'26 | 基于逐受害行计数的 RowHammer 缓解架构 |
| 21 | From Lab to Fleet: Building and Deploying a Practical Rowhammer Defense in Cloud SoCs（Microsoft） | ISCA'26 | 云 SoC 上实用 RowHammer 防御的落地部署 |
| 22 | Orthrus: Efficient and Timely Detection of Silent User Data Corruption in the Cloud with Resource-Adaptive Computation Validation | SOSP'25 | 云端用户静默数据损坏的高效及时检测 |
| 23 | Fawkes: Finding Data Durability Bugs in DBMSs via Recovered Data State Verification | SOSP'25 | 通过恢复数据状态验证发现数据库持久性 Bug |
| 24 | Optimistic Recovery for High-Availability Software via Partial Process State Preservation | SOSP'25 | 基于部分进程状态保存的高可用乐观恢复 |

---

## 第 17 周 · 12-25

### Session 5 · 数据中心资源调度（第 1–2 节）

| # | 论文 | 会议 | 一句话方向 |
|:--:|---|:--:|---|
| 25 | COpter: Efficient Large-Scale Resource-Allocation via Continual Optimization | SOSP'25 | 基于持续优化的高效大规模资源分配 |
| 26 | Moirai: Optimizing Placement of Data and Compute in Hybrid Clouds | SOSP'25 | 混合云中数据与算力放置优化 |
| 27 | Tai Chi: A General High-Efficiency Scheduling Framework for SmartNICs in Hyperscale Clouds | SOSP'25 | 超大规模云中 SmartNIC 的高效通用调度框架 |
| 28 | Sailor: Automating Distributed Training over Dynamic, Heterogeneous, and Geo-distributed Clusters | SOSP'25 | 动态异构地理分布集群上的分布式训练自动化 |
| 29 | Unlocking True Elasticity for the Cloud-Native Era with Dandelion | SOSP'25 | 云原生时代的真弹性 |
| 30 | Spirit: Fair Allocation of Interdependent Resources in Remote Memory Systems | SOSP'25 | 远程内存系统中相互依赖资源的公平分配 |

### Session 6 · 数据中心能效与散热（第 3–4 节）

| # | 论文 | 会议 | 一句话方向 |
|:--:|---|:--:|---|
| 31 | Prometheus: Toward Resilient Datacenters through Optimized Cooling Infrastructure（Google） | ISCA'26 | 优化冷却基础设施构建韧性数据中心 |
| 32 | R2D2: Robotized Reconfigurable Network for Disaggregated Datacenters | ISCA'26 | 面向解聚数据中心的机器人可重构网络 |
| 33 | Power Sloshing in Compound Servers for Large-Scale AI Inference Workloads（Meta） | ISCA'26 | 大规模 AI 推理负载下复合服务器的功耗波动 |
| 34 | PowerGrad: Hierarchical Power Management for Power-Limited ML Inference Clusters | ISCA'26 | 功耗受限 ML 推理集群的分层功耗管理 |
| 35 | PowerWeave: Unlocking Energy-Efficient ML on GPUs with OS-Level Spatial Power Management | ISCA'26 | OS 级空间功耗管理提升 GPU 上 ML 能效 |
| 36 | Rearchitecting the Datacenter Lifecycle for AI（Microsoft Azure） | ISCA'26 | 面向 AI 重构数据中心生命周期 |

---

## 选题须知

1. **每组 2–3 人**，认领 1 篇论文；36 篇须全部有人认领，全班 80 人均需参与。
2. **选题原则**：按兴趣方向自选（存储 / 闪存 / 内存 CXL / 可靠性 / 调度 / 能效散热六大方向）；同一 session 内 6 篇来自不同技术路线，认领后所在"区"与对抗配对**上课前公布**，请勿提前沟通问答内容。
3. **准备要求**（详细模板见课堂发放的 AI 提示词模板）：
   - 报告者：12 分钟讲清"核心 claim + 关键设计 + 一个代表实验"；
   - 对抗组：AI 基准问题保底 + 每组自带 1 个真正想问的尖锐问题（自主追问权重更高）。
4. **全文获取**：论文标题已逐字核实，按标题在会议官网 / 学校图书馆 / IEEE Xplore 检索即可；获取受阻及时找助教（有备援论文池）。
