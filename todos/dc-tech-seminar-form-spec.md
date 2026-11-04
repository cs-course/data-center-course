# 收集表搭建规格 · 数据中心技术论文研讨课选题意向

> 已建好空表：`https://docs.qq.com/form/page/DUGJGcWVTaExmd2dt`（file_id `PbFqeShLfwgm`）
> 本文件给你（教师/助教）用：按下面的「题目 + 选项 + 设置」在 UI 里 2 分钟搭完即可发布。
> 学生端看到的说明见同级 `dc-tech-seminar-student-guide.md`。

---

## 一、题目设置（共 6 题）

| # | 题型 | 题名 | 必填 | 说明 |
|---|---|---|:--:|---|
| 1 | 填空（短文本） | 组员1学号 | 是 | 8 位学号，如 M202674587 |
| 2 | 填空（短文本） | 组员2学号 | 是 | |
| 3 | 填空（短文本） | 组员3学号 | 否 | **仅三人组填写**，两人组留空 |
| 4 | 单选（36 选项） | 首选论文 | 是 | 选项见下方「块A」 |
| 5 | 单选（36 选项） | 备选论文1 | 是 | 选项见下方「块B」 |
| 6 | 单选（36 选项） | 备选论文2 | 是 | 选项见下方「块C」 |

> 单选每题 36 个选项，**支持整段粘贴**：编辑题目时点「批量添加选项 / 换行分隔」，把对应块一次性粘入即可。
> 三题选项内容相同（都是 1–36 号论文），只是语义不同（首选/备选1/备选2）。

## 二、表单设置（发布前核对）

- **每人限填 1 次**：开启（防止同一人重复提交；若同一个人出现在两份提交里，后续脚本交叉核对名册会抓出）
- **允许修改**：开启（截止前学生可改志愿）
- **截止时间**：设为选题截止日当天 23:59（示例：2026-11-13 周五前）
- **结果关联表格**：开启（自动生成「收集结果」在线表，截止后我读取它跑分配）
- **填写名单（选填）**：可把 `数据中心技术1班学生名单` 导入作参考，但**权威的"谁没参与"以学号 vs 80 人名册交叉核对为准**（见学生须知 + 分配脚本）

## 三、选项粘贴块

### 块A / 块B / 块C（三题通用，各粘一次）

1. Mantle: Efficient Hierarchical Metadata Management for Cloud Object Storage Services
2. ACOS: Apple's Geo-Distributed Object Store at Exabyte Scale
3. Managing Scalable Direct Storage Accesses for GPUs with GoFS
4. Rearchitecting the Thread Model of In-Memory Key-Value Stores with μTPS
5. Running Consistent Applications Closer to Users with Radical for Lower Latency
6. "Range as a Key" is the Key! Fast and Compact Cloud Block Store Index with RASK
7. LOONG: Utilizing Long-Stride Reprogramming to Enhance the Performance of SSDs
8. BoostX-NTI: Fast, Scalable and Flexible Storage Architecture with NVMe/TCP Initiator Acceleration
9. DPAS: A Prompt, Accurate and Safe I/O Completion Method for SSDs
10. Aeolia: A Fast and Secure Userspace Interrupt-Based Storage Stack
11. Sleeping with One Eye Open: Fast, Sustainable Storage with Sandman
12. SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs
13. Vistara: Making CXL Real—Full Path from ASIC Design and OS Support to Hyperscale Deployment
14. Oasis: Pooling PCIe Devices Over CXL to Boost Utilization
15. HBM-CASO: A Coordinated Approach to HBM System-Level and On-Die ECC
16. Scalable Far Memory: Balancing Faults and Evictions
17. Five-Minute Rule 40 Years Later: A First-Principles Revisit for Modern Memory Hierarchy
18. Demeter: A Scalable and Elastic Tiered Memory Solution for Virtualized Cloud via Guest Delegation
19. ColumnKeeper: Efficient Solutions to the ColumnDisturb Vulnerability in DRAM-based Systems
20. PVAC: A RowHammer Mitigation Architecture Exploiting Per-victim-row Counting
21. From Lab to Fleet: Building and Deploying a Practical Rowhammer Defense in Cloud SoCs
22. Orthrus: Efficient and Timely Detection of Silent User Data Corruption in the Cloud with Resource-Adaptive Computation Validation
23. Fawkes: Finding Data Durability Bugs in DBMSs via Recovered Data State Verification
24. Optimistic Recovery for High-Availability Software via Partial Process State Preservation
25. COpter: Efficient Large-Scale Resource-Allocation via Continual Optimization
26. Moirai: Optimizing Placement of Data and Compute in Hybrid Clouds
27. Tai Chi: A General High-Efficiency Scheduling Framework for SmartNICs in Hyperscale Clouds
28. Sailor: Automating Distributed Training over Dynamic, Heterogeneous, and Geo-distributed Clusters
29. Unlocking True Elasticity for the Cloud-Native Era with Dandelion
30. Spirit: Fair Allocation of Interdependent Resources in Remote Memory Systems
31. Prometheus: Toward Resilient Datacenters through Optimized Cooling Infrastructure
32. R2D2: Robotized Reconfigurable Network for Disaggregated Datacenters
33. Power Sloshing in Compound Servers for Large-Scale AI Inference Workloads
34. PowerGrad: Hierarchical Power Management for Power-Limited ML Inference Clusters
35. PowerWeave: Unlocking Energy-Efficient ML on GPUs with OS-Level Spatial Power Management
36. Rearchitecting the Datacenter Lifecycle for AI

---

## 四、截止后怎么出结果（教师/助教操作）

1. 关闭收集，导出「收集结果」表（含 6 列：组员1/2/3学号、首选、备选1、备选2）。
2. 整理成提交 CSV，列名固定为：`group_id, m1, m2, m3, pref1, pref2, pref3`
   - `group_id` 可留空（脚本自动编号）；`m3` 两人组留空。
   - `pref1/2/3` 填论文**编号 1–36**（不是标题）。
3. 跑分配脚本：
   ```bash
   python3 assign_papers.py submissions.csv --out assignment_result.csv
   ```
4. 脚本输出：36 组 → 36 篇的一一对应（**每篇必有一组**），并打印满足度统计 + 冲突报告。
5. 把 `assignment_result.csv` 的「分配论文」写回选题总表 `docs.qq.com/sheet/DUEJuWVJ2ZmxYVWZk` 的「报告人」列。

> 分配算法保证：组数=论文数=36 时，36 篇每篇恰好一组，不会出现某 session 论文数 ≠ 6，课堂总时长恒定。
> 已用 200 次随机 + 极端场景自测通过（详见 `assign_papers.py --self-test`）。
