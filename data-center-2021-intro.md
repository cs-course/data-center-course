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

## 应用服务的规模化

刚刚发生的事情背后，在腾讯公司的平台上

---

## 信息系统的规模化

仓库式计算机的提出

---

## 新基建

行业的发展，国家的重视

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

![3steps](images/3steps.png)

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
    - <https://prometheus.io/>, 
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

## 数据中心的日常

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
