# 数据中心技术 · 论文研讨课排期表（红蓝对抗制）

> 课程：数据中心技术（军山课堂，专业硕士 80 人）
> 研讨周：第 15 / 16 / 17 周，**12-11 / 12-18 / 12-25**（均周五下午 4 节连堂，A2-B106）
> 会议范围：CCF-A —— FAST / ATC / OSDI / SOSP / ISCA / HPCA（2025~26）
> 制定日期：2026-10-20

---

## 一、总体结构

| 维度 | 数值 | 说明 |
|---|---|---|
| 总篇数 | **36 篇** | 3 周 × 12 篇/周 |
| 总课时 | **12 课时** | 3 周 × 4 节/周；每 2 课时 = 1 session |
| 专题领域（session） | **6 个** | 每 session 6 篇，红区 3 + 蓝区 3 |
| 小组 | **2–3 人/篇** | 36 篇 × ~2.2 人 ≈ 79 人，覆盖 80 人 |
| 单篇时间 | **12 min 报告 + 3 min 对抗** | 6 篇 = 90 min / session |
| session 收尾 | **~10 min** | 红蓝小结 + 跨区总结 |

**时间轴（单个 session = 2 节 ≈ 90–100 min）**

```
[红区 3 篇: 12+3]×3 = 45 min
   └ 蓝区代表现场提问（红蓝交火）
[蓝区 3 篇: 12+3]×3 = 45 min
   └ 红区代表现场提问
[红蓝对照小结 + 跨区结论]  ~10 min
```

---

## 二、6 个专题领域与对抗轴

| Session | 专题领域 | 对应课程讲座 | 红区路线 | 蓝区路线 | 对抗轴 |
|:---:|---|---|---|---|---|
| S1 | **对象存储与元数据** | 对象存储系统与尾延迟 | 元数据/分层架构 | 运行时/线程模型低延迟 | 存储元数据架构 vs 运行时调度 |
| S2 | **固态存储与闪存管理** | 数据中心固态存储技术 | SSD 固件/设备层 | 主机存储栈 + AI 负载 | 设备层优化 vs 主机栈优化 |
| S3 | **内存层次与 CXL/HBM 互联** | v2：超大规模算力互联 | CXL 硬件/部署 | OS 内存分层/调度 | 硬件互联 vs OS 分层 |
| S4 | **可靠性与故障检测/预测** | 磁盘故障预测 + 可靠性保障 | 硬件级纠错/Rowhammer | 系统级检测/恢复 | 硬件防护 vs 系统检测 |
| S5 | **数据中心资源调度** | 概述 / 中国算力网 | 大规模集中优化 | 弹性/异构分布式 | 集中优化 vs 弹性分布式 |
| S6 | **数据中心能效与散热** | 供电与冷却 | 电力/散热基础设施 | OS 级/负载感知功耗管理 | 基础设施 vs 软件功耗管理 |

> 设计原则：同 session 6 篇**尽量来自不同课题组/不同路线**，红蓝分区时保证两条技术路线有张力，让"对抗"成为**路线之争**而非"找茬"。

---

## 三、逐 Session 论文明细

> 标注说明：**✅** = 会议与标题已逐篇核实（SOSP'25 / ISCA'26 / FAST'26 / ATC'25 / OSDI'26 完整清单）。36 篇全部落到真实篇目，无缺口。

### Week 15 · 12-11

**S1 对象存储与元数据**（第 1–2 节）

| 区 | # | 论文 | 会议 | 状态 |
|:--:|:--:|---|---|:--:|
| 🔴 红 | 1 | Mantle: Efficient Hierarchical Metadata Management for Cloud Object Storage Services | SOSP'25 | ✅ |
| 🔴 红 | 2 | ACOS: Apple's Geo-Distributed Object Store at Exabyte Scale | FAST'26 | ✅ |
| 🔴 红 | 3 | Managing Scalable Direct Storage Accesses for GPUs with GoFS | SOSP'25 | ✅ |
| 🔵 蓝 | 4 | Rearchitecting the Thread Model of In-Memory Key-Value Stores with μTPS | SOSP'25 | ✅ |
| 🔵 蓝 | 5 | Running Consistent Applications Closer to Users with Radical for Lower Latency | SOSP'25 | ✅ |
| 🔵 蓝 | 6 | "Range as a Key" is the Key! Fast and Compact Cloud Block Store Index with RASK | FAST'26 | ✅ |

**S2 固态存储与闪存管理**（第 3–4 节）

| 区 | # | 论文 | 会议 | 状态 |
|:--:|:--:|---|---|:--:|
| 🔴 红 | 7 | LOONG: Utilizing Long-Stride Reprogramming to Enhance the Performance of SSDs | ISCA'26 | ✅ |
| 🔴 红 | 8 | BoostX-NTI: Fast, Scalable and Flexible Storage Architecture with NVMe/TCP Initiator Acceleration | ISCA'26 | ✅ |
| 🔴 红 | 9 | DPAS: A Prompt, Accurate and Safe I/O Completion Method for SSDs | FAST'26 | ✅ |
| 🔵 蓝 | 10 | Aeolia: A Fast and Secure Userspace Interrupt-Based Storage Stack | SOSP'25 | ✅ |
| 🔵 蓝 | 11 | Sleeping with One Eye Open: Fast, Sustainable Storage with Sandman | SOSP'25 | ✅ |
| 🔵 蓝 | 12 | SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs | FAST'26 | ✅ |

---

### Week 16 · 12-18

**S3 内存层次与 CXL/HBM 互联**（第 1–2 节）

| 区 | # | 论文 | 会议 | 状态 |
|:--:|:--:|---|---|:--:|
| 🔴 红 | 13 | Vistara: Making CXL Real—Full Path from ASIC Design and OS Support to Hyperscale Deployment（Meta） | ISCA'26 | ✅ |
| 🔴 红 | 14 | Oasis: Pooling PCIe Devices Over CXL to Boost Utilization | SOSP'25 | ✅ |
| 🔴 红 | 15 | HBM-CASO: A Coordinated Approach to HBM System-Level and On-Die ECC | ISCA'26 | ✅ |
| 🔵 蓝 | 16 | Scalable Far Memory: Balancing Faults and Evictions | SOSP'25 | ✅ |
| 🔵 蓝 | 17 | Five-Minute Rule 40 Years Later: A First-Principles Revisit for Modern Memory Hierarchy | ISCA'26 | ✅ |
| 🔵 蓝 | 18 | Demeter: A Scalable and Elastic Tiered Memory Solution for Virtualized Cloud via Guest Delegation | SOSP'25 | ✅ |

**S4 可靠性与故障检测/预测**（第 3–4 节）

| 区 | # | 论文 | 会议 | 状态 |
|:--:|:--:|---|---|:--:|
| 🔴 红 | 19 | ColumnKeeper: Efficient Solutions to the ColumnDisturb Vulnerability in DRAM-based Systems | ISCA'26 | ✅ |
| 🔴 红 | 20 | PVAC: A RowHammer Mitigation Architecture Exploiting Per-victim-row Counting | ISCA'26 | ✅ |
| 🔴 红 | 21 | From Lab to Fleet: Building and Deploying a Practical Rowhammer Defense in Cloud SoCs（Microsoft） | ISCA'26 | ✅ |
| 🔵 蓝 | 22 | Orthrus: Efficient and Timely Detection of Silent User Data Corruption in the Cloud with Resource-Adaptive Computation Validation | SOSP'25 | ✅ |
| 🔵 蓝 | 23 | Fawkes: Finding Data Durability Bugs in DBMSs via Recovered Data State Verification | SOSP'25 | ✅ |
| 🔵 蓝 | 24 | Optimistic Recovery for High-Availability Software via Partial Process State Preservation | SOSP'25 | ✅ |

---

### Week 17 · 12-25

**S5 数据中心资源调度**（第 1–2 节）

| 区 | # | 论文 | 会议 | 状态 |
|:--:|:--:|---|---|:--:|
| 🔴 红 | 25 | COpter: Efficient Large-Scale Resource-Allocation via Continual Optimization | SOSP'25 | ✅ |
| 🔴 红 | 26 | Moirai: Optimizing Placement of Data and Compute in Hybrid Clouds | SOSP'25 | ✅ |
| 🔴 红 | 27 | Tai Chi: A General High-Efficiency Scheduling Framework for SmartNICs in Hyperscale Clouds | SOSP'25 | ✅ |
| 🔵 蓝 | 28 | Sailor: Automating Distributed Training over Dynamic, Heterogeneous, and Geo-distributed Clusters | SOSP'25 | ✅ |
| 🔵 蓝 | 29 | Unlocking True Elasticity for the Cloud-Native Era with Dandelion | SOSP'25 | ✅ |
| 🔵 蓝 | 30 | Spirit: Fair Allocation of Interdependent Resources in Remote Memory Systems | SOSP'25 | ✅ |

**S6 数据中心能效与散热**（第 3–4 节）

| 区 | # | 论文 | 会议 | 状态 |
|:--:|:--:|---|---|:--:|
| 🔴 红 | 31 | Prometheus: Toward Resilient Datacenters through Optimized Cooling Infrastructure（Google） | ISCA'26 | ✅ |
| 🔴 红 | 32 | R2D2: Robotized Reconfigurable Network for Disaggregated Datacenters | ISCA'26 | ✅ |
| 🔴 红 | 33 | Power Sloshing in Compound Servers for Large-Scale AI Inference Workloads（Meta） | ISCA'26 | ✅ |
| 🔵 蓝 | 34 | PowerGrad: Hierarchical Power Management for Power-Limited ML Inference Clusters | ISCA'26 | ✅ |
| 🔵 蓝 | 35 | PowerWeave: Unlocking Energy-Efficient ML on GPUs with OS-Level Spatial Power Management | ISCA'26 | ✅ |
| 🔵 蓝 | 36 | Rearchitecting the Datacenter Lifecycle for AI（Microsoft Azure） | ISCA'26 | ✅ |

---

## 四、红蓝对抗机制

1. **AI 预生成对抗问题**（课前 1–2 天）
   - 喂给 AI：**本 session 全部 6 篇**（不只自己那 3 篇）+ 课程目标
   - 要求 AI 站在**对方区**立场，从三个维度各出 1–2 问：
     - 方法论对比（"你这篇和 X 篇在 Y 上的取舍不同，为什么？"）
     - 实验设置差异（负载/数据集/规模的代表性）
     - 结论适用边界（什么场景下你的方案会失效？）
   - 提示词 ≤ 100 字，避免"用户主导质疑"（沿用课堂 baseline 原则）

2. **上课宣布配对**（防表演）
   - AI 问题**课前不发**到具体学生，只发到区
   - 上课时才宣布"红区第 N 篇 vs 蓝区第 M 篇"的配对，压缩预先沟通时间
   - 双轨：AI 基准问题保底 + **允许每组自带 1 个真正想问的尖锐问题**（自主追问权重更高）

3. **双轨对抗（已定稿）**
   - **AI 基准问题保底**：每组拿到 AI 预生成的 3 个基准问题（方法论对比 / 实验设置 / 适用边界各 1），保证人人有问、不打空
   - **自主追问加分**：允许/鼓励每组在上课前额外准备 **1 个自己真正想问的尖锐问题**；评分时自主追问质量权重 **高于** AI 问题
   - 设计意图：AI 问题保底（防"不会问"），自主追问逼深度（防"念 AI 问题走流程"），延迟配对防表演

4. **AI 提示词模板（已出，见配套文件）**
   - 学生用：`todos/seminar-ai-prompt-templates.md`（含论文深读模板 + 对抗提问模板 + 报告打磨模板，针对"同学 AI 使用水平参差"统一底线）
   - 教师/助教用：对抗问题批量生成模板（喂 6 篇 + 课程目标，按红蓝立场各出 3 问）

5. **评分（待补 rubric，见下节）**
   - 报告者 / 提问者 / 现场评审 三方分别打分

---

## 五、待办与缺口

> ✅ **36 篇全部落实真实篇目**（FAST'26 / ATC'25 / OSDI'26 三源已逐篇核实，2 个原缺口已补），无论文缺口。

| 项 | 内容 | 优先级 | 状态 |
|---|---|:--:|:--:|
| ~~补 2 篇~~ | S1 蓝区第 6 篇 → RASK（FAST'26）；S2 红区第 9 篇 → DPAS（FAST'26） | 高 | ✅ 已补 |
| ~~核 2 篇~~ | ACOS / SolidAttention 英文全称已从 FAST'26 程序页核实 | 中 | ✅ 已核 |
| 出 rubric | 报告者/提问者/评审三方评分标准，提前公布 | 高 | ⬜ 待出 |
| ~~出 AI 问题 prompt~~ | 红蓝对抗问题生成模板（含"对方区 3 篇"上下文） | 中 | ✅ 已出 |
| 80 人分组 | 36 组 × 2–3 人的具体名单（结合选课名单） | 中 | ⬜ 待名单 |
| 陪审团机制 | 每 session 随机抽 2–3 名非报告学生当"评审"打分（逼听众认真听） | 低 | ⬜ 待细化 |

> **程序页说明**：FAST'26 / ATC'25 / OSDI'26 三个 technical-sessions 页面已由你手工抓取并**逐篇核实**（存于 `d:\tmp\`）；SOSP'25（sigops.org）、ISCA'26（iscaconf.org）此前已完整抓取。六会清单全部为真实逐篇来源，无编造。ATC'26 未开（全文未上官网）未纳入。

> **2026-10-21 逐篇回源复核**：36 篇主表 + 备援池全部按官方源逐字核对，共纠正 **6 处**：
> ① LOONG：`Reprogram`→`Reprogramming`（ISCA'26 官网程序页系笔误，**以 IEEE Xplore 正式库为准**，doc 11617485）；
> ② GoFS：原误用「系统名: 描述」，改官方格式 `Managing Scalable Direct Storage Accesses for GPUs with GoFS`；
> ③ Radical：改官方格式 `Running Consistent Applications Closer to Users with Radical for Lower Latency`；
> ④ Dandelion：改官方格式 `Unlocking True Elasticity for the Cloud-Native Era with Dandelion`；
> ⑤ Orthrus：补全尾部 `with Resource-Adaptive Computation Validation`（原漏）；
> ⑥ 备援池 Z-LFS：补全尾部 `for Commodity Small-zone ZNS SSDs`（原漏）。
> 其余 30 篇主表标题逐字无误（ACOS 的 `Apple's` 官网用弯引号，表中用直引号，属排版差异，不影响检索）。

---

## 六、数据来源

| 会议 | 清单来源 | 覆盖 |
|---|---|---|
| SOSP'25 | sigops.org 完整日程（逐篇） | S1/S3/S4/S5 主力 |
| ISCA'26 | iscaconf.org 完整日程（逐篇） | S2/S3/S4/S6 主力 |
| FAST'26 | USENIX 程序页（手工抓取，逐篇） | S1/S2 关键篇（ACOS/RASK/DPAS/SolidAttention） |
| ATC'25 | USENIX 程序页（手工抓取，逐篇） | 备援池（本轮未直接采用，见下） |
| OSDI'26 | USENIX 程序页（手工抓取，逐篇） | 备援池（本轮未直接采用，见下） |

> **备援论文池**（ATC'25 / OSDI'26 中方向契合、可作替补的强候选，供某篇获取受阻或分组调整时替换）：
> - 存储/元数据：`Oxbow: A Coordinated Architecture for Multi-Component File Systems`（OSDI'26）、`HotRAP: Hot Record Retention and Promotion for LSM-trees with Tiered Storage`（ATC'25）、`CETOFS: A High-Performance File System with Host-Server Collaboration for Remote Storage`（FAST'26）
> - 可靠性/故障：`Understanding and Detecting Fail-Slow Hardware Failure Bugs in Cloud Systems`（ATC'25）、`FiDe: Reliable and Fast Crash Failure Detection to Boost Datacenter Coordination`（ATC'25）、`SMARTTalk: Teaching SMART Logs to Talk to LLMs`（OSDI'26）
> - 内存/CXL：`MEGALON: Efficient Data Sharing for Partly Coherent CXL Memory`（OSDI'26）、`MAC: Metadata Acceleration for Sustainable Performance in Big-Data Systems with CXL DRAM`（OSDI'26）
> - 能效/资源：`Kareus: Joint Reduction of Dynamic and Static Energy in Large Model Training`（OSDI'26）、`Hardware Lifecycle-Aware Power Planning in Commercial Hyperscale Datacenters`（OSDI'26）
> - SSD 设备：`Unleashing Zoned UFS: Cross-Layer Optimizations for Next-Generation Mobile Storage`（FAST'26）、`Z-LFS: A Zoned Namespace-tailored Log-structured File System for Commodity Small-zone ZNS SSDs`（ATC'25）
