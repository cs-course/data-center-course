---
marp: true
theme: gaia
title: 大数据存储系统与管理实验
# size: 4:3
math: katex
---

<!-- _class: lead -->

# 大数据存储系统与管理</br>对象存储技术实验

**施展**
武汉光电国家研究中心 & 计算机学院
华中科技大学
2025-05-09 (第12周周五) 至 2025-05-30 (第15周周五)
19:00~22:20 @ 南一楼803

---

## 授课教师

- **施展** 副教授，武汉光电国家研究中心，存储部，C523
- 联系方式
  - EMail <zshi@hust.edu.cn>
  - 电话 027-87792450
  - 主页
    - <https://shizhan.github.io/>
    - <http://faculty.hust.edu.cn/shizhan/zh_CN/index.htm>

---

<!-- paginate: true -->

## 背景知识

```python
if not 学习过"缺失的一课"，至少第6讲:
    if not 独立维护过Github或Gitee等开放Git仓库:
        随我进行课堂练习
```

[计算机教育中缺失的一课](https://missing-semester-cn.github.io/)，[官网](https://missing.csail.mit.edu/)，[B站](https://www.bilibili.com/video/BV1x7411H7wa/)

与本次课程相关的基础训练

- 1/13: 课程概览与 shell
- 1/14: Shell 工具和脚本
- 1/22: 版本控制([Git](https://git-scm.com/download))

---

## 学习内容

- **Lab 0** (05-09) **准备**
  - 按照要求建立实验环境，熟悉基本工具环境
- **Lab 1** (05-16) **实践**
  - 搭建使用对象存储系统，实践命令行与API基本功能
- **Lab 2** (05-23) **分析**
  - 观测对象存储基本功能，尝试分析经典性能问题
- **Lab 3** (05-30) **预测**
  - 采集观测典型性能指标，尝试建模进行预测

---

### Lab 0 建立实验环境

<style scoped>
  li {
    font-size: 30px;
  }
</style>

- [背景知识](object-storage)
- [实验参考](https://github.com/cs-course/obs-tutorial)
- 搭系统苦手？
  - 推荐用LLM工具辅助
    - <https://kimi.moonshot.cn/>
    - <https://chat.deepseek.com/>

---

#### 学号目录 README.md 模板

```Markdown
姓名：XXX
班级：xxxx班
学号：XXXXXXXX

# 实验简介

……

# 实验内容

## 实验1：……
……

# 实验小结

……
```

---

### Lab 1 搭建对象存储

- 目标系统
  - [Minio](https://minio.io/)， 简便易上手
  - [mock-s3](https://github.com/ShiZhan/mock-s3)，了解后台基本功能
  - [Ceph](https://ceph.com/)，生产环境标杆
- 搭建示范
  - [Ceph单机版](https://gitee.com/shi_zhan/data-center-course/blob/master/ceph-deployment-simple.md)

---

#### 实践基本功能

<style scoped>
  table, li {
    font-size: 27px;
  }
</style>

- 在计算机领域中，[create, read, update, and delete (缩写为 CRUD)](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) 是访问持久存储的4项基本操作。

|    Operation     |  SQL   |        HTTP        |
| :--------------  | :----  | :----------------  |
|      Create      | INSERT |     PUT / POST     |
| Read (Retrieve)  | SELECT |        GET         |
| Update (Modify)  | UPDATE | PUT / POST / PATCH |
| Delete (Destroy) | DELETE |       DELETE       |

- 通过典型界面访问在搭建的系统，执行上述典型操作
  - 客户端: [MinIO Client (mc)](https://github.com/minio/mc), [OSM](https://github.com/appscode/osm), [s3cmd](https://github.com/s3tools/s3cmd), [aws-{cli\|shell}](https://github.com/awslabs/aws-shell)
  - 编程API: [boto3](https://github.com/boto/boto3), [aws-c-s3](https://github.com/awslabs/aws-c-s3), [awssdk-rust](https://github.com/awslabs/aws-sdk-rust)

---

#### 【扩展探索】应用集成

通过部署实际应用来了解对象存储在云环境中的角色

- 个人云 [Nextcloud](https://github.com/nextcloud), [Seafile](https://www.seafile.com/home/), [zfile](https://github.com/zhaojun1998/zfile)
- 图片管理 [Thumbor](http://thumbor.org/), [picfit](https://github.com/thoas/picfit)
- …更丰富应用请同学们自行探索…

---

### Lab 2 观测分析性能

实验测试工具

- [Warp](https://github.com/minio/warp)，[Minio官网参考](https://blog.min.io/how-to-benchmark-minio-warp-speedtest/#step-3-run-warp-and-launch-a-mixed-benchmark)
- [s3bench](https://github.com/cs-course/s3bench), [benchio](https://github.com/giacomoguiulfo/benchio), [s3-benchmark](https://github.com/chinglinwen/s3-benchmark) , Go语言环境
- [OSSperf](https://github.com/christianbaun/ossperf), 内部包装[s3cmd](https://github.com/s3tools/s3cmd)
- [s3-bench-rs](https://github.com/SKTT1Ryze/s3-bench-rs) , Rust语言环境
  - 感谢 [@SKTT1Ryze](https://github.com/SKTT1Ryze) 同学提供，欢迎更多同学参与！
- [COSBench](https://github.com/intel-cloud/cosbench) , Java语言环境，功能全面但过于古老，仅供参考。

---

#### 影响性能的主要因素

<style scoped>
  li {
    font-size: 30px;
  }
</style>

典型问题举例

- **对象尺寸**如何影响性能?
  - 对于熟悉的某类应用，根据其数据访问特性，怎样适配对象存储最合适?
- 如何全面观测**I/O延迟**?
  - 平均值与统计分布
- 如果客户端爆满将怎样?
  - **请求并发数**如何同时影响延迟分布和吞吐率？如何保障服务质量？
- 横向扩展系统 (Scaling Out) 效果如何?
  - 向系统中追加**更多存储设备**或服务器

---

#### 尾延迟问题

<style scoped>
  li {
    font-size: 30px;
  }
</style>

- 尾延迟为什么很重要？
  - [The Tail at Scale](https://dl.acm.org/doi/10.1145/2408776.2408794). Commun. ACM, 2013, 56(2): 74–80.
- 可以用什么方法来分析？
  - [Amdahl’s Law for Tail Latency](https://cacm.acm.org/research/amdahls-law-for-tail-latency/). Commun. ACM, 2018, 61(8): 65–72.
- 读论文苦手？
  - 继续用LLM工具辅助
    - <https://kimi.moonshot.cn/>
    - <https://chat.deepseek.com/>

---

### Lab 3 尝试建模预测

- 为**一个应用**，结合其参数
  - 预测总体**尾延迟分布**，确定与其访存行为适配的对冲百分位
- 为**一段负载**，结合其请求序列
  - 预测未来一段时间的**IOPS**，确定是否在未来使用对冲
    - 高IOPS尽量避免，低IOPS积极发起
- 为**一段负载**，结合其参数序列
  - 预测未来一段时间的**尾延迟分布**，用于指导灵活对冲的百分位阈值
- 范例: [构建多模态模型，生成主机观测指标学习赛](https://tianchi.aliyun.com/competition/entrance/532270)

---

## 评分构成

<style scoped>
  table {
    width: 100%;
    font-size: 30px;
  }
  li {
    font-size: 20px;
  }
  p {
    font-size: 25px;
  }
</style>

| $组成部分$ | $基础$ | $进阶_1$ | $困难_2$ |
| :--- | :--- | :--- | :--- |
| $Server$ | Minio Server | mock-s3 | Ceph |
| $Client$ | Minio Client | osm/s3cmd/aws-{cli\|shell} | boto3/awssdk |
| $Benchmark_3$  | 预置负载范例 | 选题观察分析 | 编制实验程序研究 |
| **评分标准** | 每项**25分** | 每项**30分** | 每项**35分** |

1. 提供**有限课堂帮助**，[实验参考](https://github.com/cs-course/obs-tutorial)库内提供在线资源传送门。
2. 超过本资料库所提供导引之外部分**请自己探索**。
3. s3bench/benchio/COSBench……

实验方案示例1：Minio Server (25) + boto3 (35) + 延迟分布随并发数的变化趋势分析 (35)=95分
实验方案示例2：mock-s3 (30) + osm (30) + run-s3bench.cmd (25)=85分

---

## 作业提交

<style scoped>
  h3 {
    font-size: 30px;
  }
  p {
    font-size: 25px;
  }
  li {
    font-size: 18px;
  }
</style>

在微助教中完成**实验报告**。

每周的**课堂学习也会要求交一份作业**，请上传进微助教。

### 提交日期

第16周周五：**2025-06-06**

### 提交内容

课堂部分，华老师会在05-22课堂给出报告要求。

实验部分，请同学们按照前述要求用Markdown编写，上传微助教账号，提交作业。

---

### 往年作业参考

<style scoped>
  li {
    font-size: 20px;
  }
</style>

- <https://github.com/cs-course/bigdata-storage-experiment-assignment-2023>
- <https://github.com/cs-course/bigdata-storage-experiment-assignment-2022>
- <https://github.com/cs-course/iot-storage-experiment-assignment-2021>
- <https://github.com/cs-course/iot-storage-experiment-assignment-2020>
- <https://github.com/cs-course/iot-storage-experiment-assignment-2019>
- <https://github.com/cs-course/iot-storage-experiment-assignment-2018>

#### 模范作业

- [bigdata-storage-experiment-assignment-2023/U202015630](https://github.com/cs-course/bigdata-storage-experiment-assignment-2023/tree/main/U202015630/)
- [bigdata-storage-experiment-assignment-2023/U202015628](https://github.com/cs-course/bigdata-storage-experiment-assignment-2023/tree/main/U202015628/)
- [bigdata-storage-experiment-assignment-2022/U201916202](https://github.com/cs-course/bigdata-storage-experiment-assignment-2022/tree/master/U201916202/)
- [bigdata-storage-experiment-assignment-2022/U201915084](https://github.com/cs-course/bigdata-storage-experiment-assignment-2022/tree/master/U201915084/)
- [iot-storage-experiment-assignment-2021/U201816030](https://github.com/cs-course/iot-storage-experiment-assignment-2021/tree/master/U201816030)
