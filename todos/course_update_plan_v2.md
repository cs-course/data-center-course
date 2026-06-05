# 下学期教学内容更新计划 (v2)

## 1. 核心目标
结合近期文摘中涌现的 **"AI-Native Infrastructure"** (AI原生基础设施) 趋势，将教学重心从传统的通用系统架构转向 **"计算-存储-连接" 三位一体的智能系统设计**。

## 2. 教学任务匹配与内容模块

### 🎓 任务一：数据中心技术课堂 (Data Center Technology)
**核心逻辑**：探讨如何支撑大规模 AI 负载（LLM/Agent）的超大规模、高吞吐、低延迟基础设施。

| 模块名称 | 结合文摘主题 | 教学重点 (Learning Objectives) |
| :--- | :--- | :--- |
| **AI 时代的存储架构** | DeepSeek 3FS, JuiceFS, 对象存储与文件存储之争 | 探讨从传统存储到 AI 专用文件系统（如 3FS）的演进；研究如何通过存储层优化解决 AI 训练/推理的 I/O 瓶颈。 |
| **计算-存储协同 (Near-Data Computing)** | PIM (存内计算), 记忆即算力, 存储级计算 | 讨论从 CPU-Centric 到 Memory/Storage-Centric 的范式转移；讲解如何在存储介质中实现初步计算以降低数据搬运。 |
| **超大规模算力互联** | NVLink, RoCE/RDMA, CXL 内存扩展 | 讲解大规模集群中的数据搬运难题；引入 CXL 协议实现内存池化与异构计算资源共享。 |
| **AI 负载调度与 QoS** | PD 分离 (Prefill-Decode Disaggregation), 负载均衡 | 深入剖析 LLM 推理过程中的计算特性；讲解如何通过 PD 分离技术提升系统吞吐量与响应稳定性。 |

---

### 🎓 任务二：计算机系统设计专题讲座 (System Design)
**核心逻辑**：从底层硬件抽象到高层软件架构，理解如何为 AI Agent 和大规模模型构建高效的执行环境。

| 模块名称 | 结合文摘主题 | 教学重点 (Learning Objectives) |
| :--- | :--- | :--- |
| **新型内存层次结构设计** | Unified Memory (GB10), CXL, KV Cache 优化 | 设计面向大模型的内存层次；探讨如何通过量化压缩 (TurboQuant) 与 KV Cache 卸载优化显存利用率。 |
| **异构加速器设计 (NPU/GPU/FPGA)** | NVIDIA GB10, OpenClaw, RISC-V AI 芯片 | 分析不同芯片架构（SIMT vs. Dataflow）在 AI 任务中的优劣；探讨 FPGA 在 AI 数据通路预处理中的角色。 |
| **AI Agent 运行环境设计** | Agentic Engineering, OpenClaw, Context Compression | 讲解 Agent 系统对操作系统/文件系统的特殊需求；设计支持长时记忆、高上下文窗口的系统架构。 |
| **高效率推理引擎实现** | SGLang, Mooncake, MoE 优化 | 深入探讨推理引擎的内部机制，包括调度策略、算子优化以及如何处理混合专家模型 (MoE) 的动态负载。 |

## 3. 过程材料说明
- **素材库**：所有教学案例均来源于 `/mnt/netbackup/collection` 的最新 Markdown 文摘。
- **实验设计**：计划结合 `Fastllm` 或 `vLLM` 进行本地实验，验证 PD 分离或 KV Cache 优化的效果。
- **保存位置**：过程记录与初步大纲已存入 `~/cs-course/todos/`。
