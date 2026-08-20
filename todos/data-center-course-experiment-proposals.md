# 数据中心技术 · 课堂实验形式与内容建议（供课程组讨论）

> 背景：下学期考虑通勤问题，课改为**每周一次、4 节连堂**。第 1 周讲背景知识，第 2~5 周各围绕一个专题授课。
> 为避免 4 节纯讲解枯燥，建议在专题周**穿插课堂实验演示（Live Demo）**，并酌情布置对应实验作业。
> 本文件检索了康奈尔、CMU、ETH、VT、乌尔姆等国外高校，以及华科本部、清华、中科大的相关课程实验形式，形成可按周次落地的建议，供课程组讨论。
>
> 说明：当前 `data-center-pre.md` 仍显示旧课表（周次 2-9 / 10-17），新课表具体日期待定。以下按"第 1 周背景 + 第 2~5 周专题"结构组织，专题主题沿用 `data-center-pre.md` 中已有的讲座主题。

---

## 一、国内外高校相关课程实验形式调研

### 1.1 康奈尔大学（Cornell）

| 课程 | 形式 | 与本课关联 |
| --- | --- | --- |
| **CS5413** Topics in Computer Systems: Data Center Networks & Systems（Hakim Weatherspoon） | **每周一次 in-class lab**（需带笔记本，当堂完成）+ take-home homework + 课程项目/BOOM；实验含：搭建网络代理（单/多线程）、chatserver、SDN 软件交换机/控制器；基础设施用自研 mini-cloud "Fractus"、NetFPGA、EC2/S3、Emulab、PlanetLab | 实验"镶嵌"进 4 节连堂的做法可直接借鉴 |
| **Datacenter Computing**（Christina Delimitrou, Spring 2020） | 半讲授半论文研讨；教科书即 **Barroso《The Datacenter as a Computer》**（与本课同款）；研究型课程，2-3 人小组做真实前沿研究项目 | 主题/教材完全一致，可作为内容参照 |

### 1.2 CMU（卡内基梅隆）

**15-719 Advanced Cloud Computing**（Greg Ganger / Majd Sakr / George Amvrosiadis）
- 评分约 **50% 项目 + 15% 测验 + 35% 考试**；获 AWS 教育资助，每人 $50 额度。
- 项目平台 TheProject.Zone，分三期：**P1** 用 OpenStack 搭建 CMU 云；**P2** 存储 / Key-Value 存储；**P3** 调度、尾延迟与干扰、可靠性容错、Kubernetes、地理复制。
- 主题覆盖：封装计算、弹性伸缩、存储、编程模型、调度、KV 存储、尾延迟、可靠性容错、监控诊断、数据中心网络、Geo-replication。
- 上课时间 MW 16:00–17:50（即两节连堂），与本课 4 节连堂节奏接近。

### 1.3 ETH Zurich（苏黎世联邦理工）

**227-0085-44L Understanding and Designing Modern Storage Systems（P&S）**
- 两部分：每周 NAND-flash SSD 讲座 + **动手项目：重构 MQSim（高端 SSD 仿真器，C++）** 支持现代 NAND 特性与 FTL 任务（地址转换、垃圾回收、磨损均衡、I/O 调度）。
- 参考教材：《Inside NAND Flash Memories》《Inside Solid State Drives》。

### 1.4 Virginia Tech（弗吉尼亚理工）

**CS5204 Operating Systems**
- Lab1 用 **FEMU**（基于 QEMU 的 NVMe SSD 模拟器，黑盒模式）配置不同通道数/芯片数布局（L1–L4），用 fio 跑 4KB 随机读 IOPS，分析内部并行度对性能的影响。
- 提供 CloudLab VM 镜像，降低环境门槛。

### 1.5 乌尔姆大学（Universität Ulm, 德国）

**Data Centre Networks Architecture and Protocols**
- 以协议规范与文献为主；练习（Exercises）让学生做存储网络/数据中心的小设计挑战，并逐步演进到为不同应用域（大数据分析、科学计算、Server Farming、云计算）设计完整数据中心系统。

### 1.6 国内高校

| 高校/课程 | 实验形式 | 可借鉴点 |
| --- | --- | --- |
| **华中科技大学·大数据存储系统与管理实验**（本部，cs-course/bigdata-storage-experiment） | 对象存储 **MinIO / Ceph / OpenStack Swift** 部署；基准工具 **s3bench、benchio、COSBench**；尾延迟分析（The Tail at Scale）；配套实验报告模板与评分 | **直接可复用**于第 2 周（对象存储+尾延迟） |
| **华中科技大学·云计算与虚拟化** | Hadoop 搭建与使用、KVM/XEN 虚拟化、EC2/S3 实测对比 | 云平台实操范式 |
| **清华大学·大数据实践课** | 校企双导师、学生组队用企业"真问题、真数据"完成实践项目；用 HDFS/Spark/Flink/IoTDB 等 | "真实数据驱动"的项目组织方式 |
| **中国科学技术大学·人工智能实训平台** | 与百度合作的 AI Studio + 本地 GPU 集群，统一认证、一键 Notebook、自动评分 | 一体化实验平台的建设思路 |

### 1.7 调研小结（对比表）

| 维度 | 康奈尔 CS5413 | CMU 15-719 | ETH 存储 P&S | 华科大数据存储实验 | 乌尔姆 DC 网络 |
| --- | --- | --- | --- | --- | --- |
| 课堂穿插实验 | ✅ 每周 in-class lab | 项目为主 | 讲座+项目 | ✅ 实验课 | 练习设计 |
| 云平台实操 | EC2/S3 | AWS $50 额度 | — | EC2/S3 | — |
| 仿真/模拟器 | Fractus/NetFPGA | — | MQSim | s3bench/COSBench | — |
| 研究/工程项目 | ✅ BOOM | ✅ 50% | ✅ MQSim 重构 | 实验报告 | 设计挑战 |
| 适配本课强度 | 中 | 高（偏重） | 中（偏底层） | **高（主题贴合）** | 中 |

---

## 二、可复用的课堂实验"形式"清单

根据调研，归纳出 7 类可在本课落地的实验形式，按"课堂内可完成度"排序：

1. **课堂 Live Demo（教师现场操作 + 学生观察记录）**——最适合 4 节连堂中途穿插，零环境门槛（教师机演示，投屏即可）。
2. **随堂动手（In-class lab / workshop）**——学生自带笔记本，当堂跑简化版（如康奈尔每周一次）。
3. **课后实验（Take-home lab）**——布置到实验报告/平台，限期提交（如华科大数据存储实验、VT CS5204）。
4. **课程项目（Course Project）**——小组做较大课题（康奈尔研究型、CMU 50% 项目）。
5. **云平台实操**——AWS / 阿里云 / 华为云额度，真实环境搭云、测对象存储、跑服务。
6. **仿真/模拟器（沙盒）**——CloudSim（数据中心调度）、ns-3（网络/故障）、FEMU（SSD）、MQSim（SSD FTL），成本低、可在学生笔记本跑。
7. **真实数据驱动**——Backblaze SMART 数据集（故障预测）、天池赛（内存故障预测），直接对接本课现有 30% 实验作业。

---

## 三、按新课表周次的具体实验建议（核心）

> 每个专题给出：演示内容 / 工具 / 学生活动 / 是否作业 / 工作量 / 参考来源。
> 难度与工作量按本课 2 学分（32 学时）控制，以"演示为主、作业酌情"为原则。

### 第 1 周 · 背景知识（数据中心作为计算机 / WSC 概览）

- **演示 1（概念可视化）**：用 **CloudSim** 创建含 2 个 host 的数据中心、跑 cloudlets，直观展示"把整个数据中心看作一台计算机"的资源调度思想（经典入门 demo，Java 即可）。
- **演示 2（真实素材）**：播放/展示真实数据中心 tour（Google Data Center）、华中科技大学武汉光电国家研究中心/集群与网格计算实验室实景，呼应"从一台机器到一个数据中心""东数西算"。
- **演示 3（可选，进阶）**：用 **minikube/k3s** 一键拉起一个多副本 Web 服务，演示"舰队即一台机器"的调度与副本漂移。
- **学生活动**：分组讨论"为什么数据中心要软件定义、为何要接受部分故障"；提交 1 页背景概念笔记。
- **是否作业**：否（或极轻量）。
- **参考**：CloudSim（GeeksforGeeks 教程）、康奈尔 Datacenter Computing 教材、华科云计算与虚拟化课 EC2/S3 实操。

### 第 2 周 · 对象存储系统与尾延迟问题

- **演示（直接复用本部资产）**：现场部署 **MinIO** 对象存储，用 **s3bench** 跑分，采集并绘制 **百分位延迟（p50/p95/p99/p99.9）**，展示长尾现象；对照《The Tail at Scale》(Dean & Barroso, 2013) 与《Amdahl's Law for Tail Latency》(Delimitrou & Kozyrakis, 2018)。
- **学生活动**：
  - 观察"对象尺寸 / 并发数"如何影响吞吐与尾延迟；
  - 给定某类应用（如图片小文件、大对象备份）的访问模式，设计对象布局与分片策略。
- **工具**：MinIO / Ceph / OpenStack Swift；s3bench、COSBench、s3-bench-rs。
- **是否作业**：**建议作为实验作业候选**（对接现有 30% 实验作业），提交基准报告 + 尾延迟分析。
- **参考**：华科 cs-course/bigdata-storage-experiment（README 已列全工具链）；jchenTech/Data-Center-Lab（K8s + 对象存储性能分析）。

### 第 3 周 · 数据中心固态存储技术（SSD）

- **演示（仿真，低成本）**：用 **FEMU** 黑盒模式配置 4 种 SSD 内部布局（通道数 1/2/4/8 × 4 chips），用 **fio** 跑 4KB 随机读 IOPS，绘制"通道数 vs IOPS"曲线，说明内部并行度；演示 GC 触发、写放大、FTL 地址映射概念（可辅以 **MQSim** 观察 GC/WL 行为）。
- **学生活动**：分析"增加并发作业数 / 增加通道数"分别如何影响性能及其原因；讨论尾延迟在 SSD 上的来源（读重试、GC 暂停）。
- **工具**：FEMU（QEMU 扩展，提供 VM 镜像）、MQSim（C++，ETH 课程用）、fio。
- **是否作业**：可选轻量——给定布局改参数复现曲线并提交解读。
- **参考**：Virginia Tech CS5204 Lab1（FEMU 4 布局 × 6 numjobs 实验）、ETH Zurich「Understanding and Designing Modern Storage Systems」(MQSim 重构)。

### 第 4 周 · 数据中心磁盘故障预测技术

- **演示（真实数据驱动）**：用 **Backblaze 公开 SMART 数据集**（20 万+ 盘每日快照）子集，在 scikit-learn 上训练**随机森林**做故障预测；当场展示**类别极度不均衡**问题（正常样本 16 万 vs 故障样本个位数），用 SMOTE / 标签平滑（回推 N 天）处理，看 precision/recall 变化。
- **学生活动**：讨论哪些 SMART 属性最关键（5 重映射扇区、187 不可纠正错误、188 命令超时、197 待映射扇区、198 离线不可纠正），以及为什么；对比传统 ML（XGBoost）与深度学习（LSTM/Transformer）的取舍。
- **工具**：Backblaze 数据集、Python(scikit-learn / XGBoost / PyTorch)、SMOTE。
- **是否作业**：**强建议对接本课现有 30% 实验作业**——课程原评分已含"天池 内存故障预测"赛，可并行提供"磁盘故障预测"实验作业（用 Backblaze 或天池数据），以完成提交上榜为准，重在实践。
- **参考**：largo.dev 硬盘故障预测教程（XGBoost/LSTM/Transformer 全流程）、华为云 ModelArts / CSDN 随机森林案例、StreamDFP（流式故障预测框架）。

### 第 5 周 · 数据中心可靠性保障技术

- **演示 1（网络层容错）**：用 **ns-3** 搭建数据中心拓扑，注入链路故障，演示**快速故障检测 + 重路由/故障转移（failover）**，用 FlowMonitor 观察业务连续性与丢包恢复。
- **演示 2（系统层自愈，可选）**：用 **Kubernetes** 演示 Pod 故障后副本自愈、跨故障域调度；结合 Erasure Coding / 多副本讨论可用性计算（如 3 副本 vs EC 的存储开销与容错）。
- **学生活动**：计算给定冗余策略下的年可用性；讨论故障域（failure domain）、SLA、副本放置。
- **工具**：ns-3（故障注入/业务连续性脚本）、Kubernetes（minikube/k3s）、CloudSim（高可用调度）。
- **是否作业**：可选——ns-3 故障注入小实验报告，或 K8s 副本容错观察记录。
- **参考**：CMU 15-719 可靠性与容错（Schneider'90, Candea'04）、ns-3 故障处理示例、CloudSim 高可用仿真。

---

## 四、4 节连堂的"穿插节奏"建议

为避免纯讲解疲劳，每个专题周建议如下节奏（可按内容弹性调整）：

| 节次 | 内容 | 形式 |
| --- | --- | --- |
| 第 1 节 | 专题核心概念与原理 | 讲授 + 案例 |
| 第 2 节 | 深入机制 / 论文要点 / 工程挑战 | 讲授 + 提问 |
| 第 3 节 | **课堂实验演示（Live Demo）** | 教师操作 + 学生观察记录 |
| 第 4 节 | **随堂动手 / 研讨** | 学生分组跑简化版或围绕演示数据讨论，教师答疑 |

> 若某专题演示偏重（如 SSD 的 FEMU、故障预测的模型训练），可把第 4 节改为"演示续 + 分组解读"，降低当场环境压力；完整实操放到课后实验。

---

## 五、可行性与资源建议（结合华科实际）

1. **复用本部已有资产**：第 2 周对象存储实验可直接复用 `cs-course/bigdata-storage-experiment` 的工具链与报告模板，几乎零新增成本。
2. **低门槛仿真器优先**：CloudSim / ns-3 / FEMU / MQSim 均可在学生笔记本或机房 VM 运行，不需真实硬件；FEMU、MQSim 都有现成镜像/仓库。
3. **云平台额度**：若做云实操，可申请 AWS Educate / 阿里云 / 华为云教育额度（CMU 模式），但需注意通勤与机房网络环境。
4. **真实数据**：Backblaze 数据集开源可直接下载；故障预测作业与现有天池赛形成"双赛道"，学生二选一或都做。
5. **环境前置**：建议在课程群发布"计算机教育中缺失的一课"（shell、Git、环境配置）作为课前准备，降低当堂动手阻力（本部实验 README 已推荐）。

---

## 六、待课程组讨论的开放问题

1. **实验作业比例**：现有评分=论文研讨 30% + 实验作业 30%（天池内存故障预测）+ 开卷考试 40%。新增"课堂演示+作业"是否从现有 30% 实验作业中分出子项，还是另行增设？
2. **演示 vs 动手的侧重**：受 4 节连堂与机房条件限制，各周以"演示为主"还是"演示+当堂动手"？
3. **工具链统一**：是否统一到 MinIO/FEMU/K8s/Backblaze + Python 这一套，降低 TA 支持成本？
4. **第 6~8 周安排**：新课表仅描述到第 5 周专题，后续论文研讨（I/II/III）与考试周是否需要保留实验元素（如"论文复现 mini-lab"）？
5. **评分与防 AI 作弊**：实验作业如何考查真实动手能力（参考课程已有"模拟 Rebuttal / 站在 AI 肩膀上而非靠着 TA"理念）？

---

## 附：参考来源

- 康奈尔 CS5413（Data Center Networks & Systems）课程大纲：https://www.cs.cornell.edu/courses/cs5413/2017sp/lectures/01-intro.pdf
- 康奈尔 Datacenter Computing（Delimitrou, 同款教材）：https://sites.google.com/view/datacentercomputingspring2020/logistics
- CMU 15-719 Advanced Cloud Computing：https://www.cs.cmu.edu/~15719 ；课程表 https://www.cs.cmu.edu/afs/cs/academic/class/15719-s18/web/syllabus.html
- ETH Zurich Understanding and Designing Modern Storage Systems（MQSim）：https://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?lerneinheitId=187232&semkez=2025S ；https://safari.ethz.ch/projects_and_seminars/fall2025/doku.php?id=modern_ssds
- Virginia Tech CS5204（FEMU 实验）：https://vtcs5204.github.io/labs.html
- 乌尔姆大学 Data Centre Networks：https://www.uni-ulm.de/in/omi/lehre/lehrangebot/data-centre-networks-architecture-and-protocols/
- 华科大数据存储实验（cs-course/bigdata-storage-experiment）：https://github.com/cs-course/bigdata-storage-experiment
- 华科云计算与虚拟化教学大纲：https://www.xiaokudang.com/docs/view/3083bb4d1ce94ecf8b4ec3f2a7d9a0af.html
- 清华大数据实践课（真问题真数据+双导师）：https://bigdata.tsinghua.edu.cn/Content/2022/11-21/1130165475.html
- 中科大 AI 实训平台：https://etcis-web.ustc.edu.cn/rgznsxpt/
- 对象存储/尾延迟：jchenTech/Data-Center-Lab（K8s + 对象存储性能分析）https://github.com/jchenTech/Data-Center-Lab ；尾延迟经典论文《The Tail at Scale》Dean & Barroso, CACM 2013
- 磁盘故障预测：Backblaze 数据集 https://www.backblaze.com/b2/hard-drive-test-data.html ；largo.dev 教程 https://largo.dev/tutorials/production-ml/hard-drive-failure-prediction ；华为云 ModelArts 随机森林案例 https://xie.infoq.cn/article/c8475c1398d12761fa14ef057
- 仿真器：CloudSim（GeeksforGeeks 教程 https://www.geeksforgeeks.org/cloud-computing-simulation-using-cloudsim/ ）、ns-3 故障处理示例 https://ns3simulation.com/how-to-implement-network-rapid-fault-handling-in-ns3/ 、FEMU https://github.com/MoatLab/FEMU 、MQSim https://github.com/CMU-SAFARI/MQSim
