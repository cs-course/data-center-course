---
marp: true
theme: gaia
title: 数据中心技术
# size: 4:3
---

# 数据中心技术简介

**施展**
武汉光电国家研究中心
光电信息存储研究部

---

## 内容大纲

- 课堂背景调查
- 数据中心技术
  - 定义、起源和历史
  - 经典案例
  - 问题和挑战
  - 发展趋势
- 学习目的
- 实践基础

---

## 课堂背景调查

<style scoped>
th {
  display: none;
}
table {
  width: 100%;
}
</style>

|   |   |
|:-:|:--|
|![h:450](images/qq-group-2021.png)|1. 扫码进群<br/>2. 参与投票|

---

## 刚刚发生的事情背后

![h:450](images/Web-Application-Architecture.png)

<https://codecondo.com/web-application-architecture/>

---

<style scoped>
table, p {
  font-size: 20px;
}
</style>

## 在腾讯公司的平台上

![h:380](images/tencent-fact-2016.png)

|全球服务器|数据存储规模|全球加速节点|带宽储备|云产品服务|
|:-:|:-:|:-:|:-:|:-:|
|100W+|EB级|2800+|200T|300+|

<https://cloud.tencent.com/about>

---

![bg](images/01-Global-Overview-DataReportal-20200422-Digital-2020-April-Global-Statshot-Report-Slide-7.png)

<!-- https://wearesocial-net.s3.amazonaws.com/uk/wp-content/uploads/sites/2/2020/04/01-Global-Overview-DataReportal-20200422-Digital-2020-April-Global-Statshot-Report-Slide-7.png -->

---

<style scoped>
p {
  padding-top: 200px;
  text-align: center;
  font-size: 72px;
  color: 0040FF;
}
</style>

![bg opacity:.3 brightness:.5](images/01-Global-Overview-DataReportal-20200422-Digital-2020-April-Global-Statshot-Report-Slide-7.png)

<!-- https://wearesocial-net.s3.amazonaws.com/uk/wp-content/uploads/sites/2/2020/04/01-Global-Overview-DataReportal-20200422-Digital-2020-April-Global-Statshot-Report-Slide-7.png -->

网络服务已渗透社会各个方面

---

![bg](images/05-Changes-in-Connected-Behaviours-DataReportal-20200422-Digital-2020-April-Global-Statshot-Report-Slide-11.png)

<!-- https://wearesocial-net.s3.amazonaws.com/uk/wp-content/uploads/sites/2/2020/04/05-Changes-in-Connected-Behaviours-DataReportal-20200422-Digital-2020-April-Global-Statshot-Report-Slide-11.png -->

---

<style scoped>
p {
  padding-top: 200px;
  text-align: center;
  font-size: 72px;
  color: 0040FF;
}
</style>

![bg opacity:.3 brightness:.5](images/05-Changes-in-Connected-Behaviours-DataReportal-20200422-Digital-2020-April-Global-Statshot-Report-Slide-11.png)

<!-- https://wearesocial-net.s3.amazonaws.com/uk/wp-content/uploads/sites/2/2020/04/05-Changes-in-Connected-Behaviours-DataReportal-20200422-Digital-2020-April-Global-Statshot-Report-Slide-11.png -->

疫情甚至加快了这个过程

---

<style scoped>
li, p {
  font-size: 20px;
}
</style>

## 随之而来的数据洪流

![w:1150](images/IDC_DataSphere.png)

<https://www.datanami.com/2018/11/27/global-datasphere-to-hit-175-zettabytes-by-2025-idc-says/>

---

![bg fit](images/IDC_edge_to_core.png)

---

<style scoped>
li, p {
  font-size: 30px;
}
</style>

## 新基建

- 国家发展改革委创新和高技术发展司2020年发布
  - 新型基础设施是以新发展理念为引领，以技术创新为驱动，以信息网络为基础，面向高质量发展需要，提供数字转型、智能升级、融合创新等服务的基础设施体系，主要包括信息基础设施、融合基础设施、创新基础设施等三方面内容。
- **信息基础设施**主要是指基于新一代信息技术演化生成的基础设施。
  - 以5G、物联网、工业互联网、卫星互联网为代表的通信网络基础设施
  - 以人工智能、云计算、区块链等为代表的新技术基础设施
  - 以**数据中心**、智能计算中心为代表的算力基础设施

<http://www.xinhuanet.com/fortune/2020-04/21/c_1125883443.htm>

---

<style scoped>
th {
  display: none;
}
h3, li, td, p {
  font-size: 14px;
}
</style>

## 信息系统的规模化趋势

### Latency Comparison Numbers

||||||
|:-|-:|-:|-:|:-|
| L1 cache reference                 |          0.5 ns |            |        |                             |
| Branch mispredict                  |          5   ns |            |        |                             |
| L2 cache reference                 |          7   ns |            |        | 14x L1 cache                |
| Mutex lock/unlock                  |         25   ns |            |        |                             |
| Main memory reference              |        100   ns |            |        | 20x L2 cache, 200x L1 cache |
| Compress 1K bytes with Zippy       |      3,000   ns |       3 us |        |                             |
| Send 1K bytes over 1 Gbps network  |     10,000   ns |      10 us |        |                             |
| Read 4K randomly from SSD*         |    150,000   ns |     150 us |        | ~1GB/sec SSD                |
| Read 1 MB sequentially from memory |    250,000   ns |     250 us |        |                             |
| Round trip within same datacenter  |    500,000   ns |     500 us |        |                             |
| Read 1 MB sequentially from SSD*   |  1,000,000   ns |   1,000 us |   1 ms | ~1GB/sec SSD, 4X memory     |
| Disk seek                          | 10,000,000   ns |  10,000 us |  10 ms | 20x datacenter roundtrip    |
| Read 1 MB sequentially from disk   | 20,000,000   ns |  20,000 us |  20 ms | 80x memory, 20X SSD         |
| Send packet CA->Netherlands->CA    |150,000,000   ns | 150,000 us | 150 ms |                             |

### Notes

1 ns = 10^-9 seconds
1 us = 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns

### Credit

By Jeff Dean: <http://research.google.com/people/jeff/>
Originally by Peter Norvig: <http://norvig.com/21-days.html#answers>

---

![bg fit](images/Latency-Numbers-Every-Programmer-Should-Know.png)

<!-- https://colin-scott.github.io/personal_website/research/interactive_latency.html -->

---

<style scoped>
li, p {
  font-size: 30px;
}
</style>

## 仓储级计算机

[路易斯·安德烈·巴罗索（Luiz André Barroso）](https://www.barroso.org/)，谷歌研究员、ACM会士、AAAS会士，领导着谷歌的工程基础设施工作。

- [Warehouse-scale Computing](https://dl.acm.org/doi/10.1145/1807167.1837133), SIGMOD '10
- [Warehouse-Scale Computing: Entering the Teenage Decade](https://dl.acm.org/doi/10.1145/2000064.2019527), ISCA '11
- [A Brief History of Warehouse-Scale Computing](https://barroso.org/publications/IEEEMicro2021.pdf), 2020 Eckert-Mauchly Award

---

## 定义、起源和历史

存储工业协会SNIA的定义

---

## 经典案例

---

## 谷歌

---

## 微软

---

## 脸书

---

## 阿里

---

## 腾讯

---

## 问题和挑战

- 可靠性
- 一致性
- 波动性
- 可用性
- 尾延迟

---

### 可靠性

---

### 一致性

---

### 波动性

---

### 可用性

---

### 尾延迟

---

## 发展趋势

绿色环保、模块化、边缘计算

---

## 学习目的

---

## 实践基础

- 建立一套数据中心实验平台
  1. Linux系统
  2. 虚拟机、容器、存储
  3. 监控管理工具
- 还有**亿点点**细节

![bg right fit](images/3steps.png)

---

## 选择合适的系统

怎么给自己准备一套便利的Linux学习环境？

- **Linux** 直接安装，多重引导
- **Mac/Win** 虚拟机、容器、编排工具
- **Win**
  - 虚拟机、容器、编排工具
  - Windows Subsystem Linux (WSL, WSL2)
  - Cygwin, MSYS (MinGW)

---

<style scoped>
li, p {
  font-size: 20px;
}
</style>

## 准备和熟悉环境

- **目标**：
  - 远程连接主机、远程执行命令
  - 检查服务器状态:
    - 发行版、内核版本、时间、网络、进程、设备、磁盘、文件系统
    - *uname, date, ifconfig, ps, /proc, /dev, df, du, mount*
  - 代码、脚本、配置管理初步
    - 版本管理 *git, github, bitbucket, gitee*
    - 文本操作 *cat, head, tail, grep, sed, awk, cut, paste, join*
  - 一两套批量部署工具 *ansible, puppet, cfengine*
    - 添加和更新软件安装源
    - 想一想，怎样提高效率？学校源 <http://mirrors.hust.edu.cn/>、本地源
  - 集群时间同步 *ntp, chrony*

---

## 命令行操作入门

- 系统状态
  - 有哪些关键目录
  - 系统信息的跟踪和采集
- 信息处理
  - 控制台文本的读写、查找、提取、统计、排序、去重、合并
- 数据处理
  - 压缩与解压缩、二进制转换
  - 特殊设备(/dev/null, /dev/zero, /dev/random)
- 工具之间的联动与**KISS原则**

---

## 初步尝试管理

- 编制Bash脚本
  - 循环、参数、管道与重定向
- 远程管理方法
  - 网络管道、文件同步、终端会话保持
- 任务执行
  - 后台执行、控制台管理
  - 定时重复、计划任务
- 配置和脚本管理
  - git与github

---

![bg cover](images/emergency.jpg)

---

![bg fit](images/keep-calm.png)

---

## 更进一步

- Dashboard仪表盘
  - Grafana
    - <https://grafana.com>
    - <https://github.com/grafana/grafana>
  - Prometheus
    - <https://prometheus.io/>
    - <https://github.com/prometheus/prometheus>
  - InfluxDB & Telegraf
    - <https://www.influxdata.com>

---

![bg fit](images/prometheus-architecture.png)

---

![bg fit](images/APM-Diagram-1.webp)

---

<style scoped>
td {
  font-size: 25px;
}
</style>

## 经典问题

|微观|宏观|环境|
|:-|:-|:-|
|*Understanding Disk Failure Rates: What Does an MTTF of 1,000,000 Hours Mean to You?*|*Failure Trends in a Large Disk Drive Population*|*Datacenter Scale Evaluation of the Impact of Temperature on Hard Disk Drive Failures*|
|![w:350](images/understanding-disk-failure.png)|![w:350](images/failure-trends.png)|![w:350](images/datacenter-scale-evaluation.png)|

---

## 后续内容

- 熟悉环境
  - *Linux, Git, SSH, Python, OpenStack, K8S, Docker* …
- 着手综述
  - 跟随讲座内容，检索和阅读论文，准备下个月汇报
- 数据中心专题讲座与实践
  - 键值存储
  - 对象存储
