---
marp: true
theme: gaia
title: 数据中心技术
# size: 4:3
---

<!-- _class: lead -->

# 数据中心技术

**施展，童薇，胡燏翀**
武汉光电国家研究中心，计算机学院
2022-11-03 至 2022-12-22

---

## 基本信息

<style scoped>
  li {
    font-size: 30px;
  }
</style>

- 课程资料 <https://github.com/cs-course/data-center-course>  
- 作业库 <https://github.com/cs-course/data-center-course-assignment-2022>
- 参考书
  - [John Hennessy](https://hennessy.stanford.edu/), [David Patterson](https://www2.eecs.berkeley.edu/Faculty/Homepages/patterson.html), [**Computer Architecture: A Quantitative Approach**, 6th Edition.](https://www.elsevier.com/books/computer-architecture/hennessy/978-0-12-811905-1), 2017
  - [**计算机体系结构：量化研究方法**（第5版）](https://item.jd.com/19082510945.html), 机械工业出版社, 2013
  - [Luiz André Barroso](https://www.barroso.org/), Urs Hölzle, and Parthasarathy Ranganathan, [**The Datacenter as a Computer: Designing Warehouse-Scale Machines**, Third Edition.](https://www.morganclaypool.com/doi/10.2200/S00874ED3V01Y201809CAC046), 2019
  - [**数据中心一体化最佳实践：设计仓储级计算机**（原书第3版）](https://book.douban.com/subject/34950732/), [美] [路易斯·安德烈·巴罗索](https://www.barroso.org/) 著，徐凌杰 译, 2020

---

## 授课教师

- **施展** 副教授，武汉光电国家研究中心，存储部，C523
- 课程公务 每周五上午08:30-10:00
- 联系方式
  - EMail zshi@hust.edu.cn
  - 电话 027-87792450
  - 主页
    - <https://shizhan.github.io/>, <https://shi_zhan.gitee.io/>
    - <http://faculty.hust.edu.cn/shizhan/zh_CN/index.htm>

---

## 授课教师…

- **童薇** 副教授，武汉光电国家研究中心，存储部，C522
- 课程公务 每周四上午08:30-10:00
- 联系方式
  - EMail tongwei@hust.edu.cn
  - 电话 027-87792450
  - 主页
    - <http://faculty.hust.edu.cn/tongwei/zh_CN/index.htm>

---

## 授课教师……

- **胡燏翀** 教授，武汉光电国家研究中心，存储部，B518
- 课程公务 每周五上午08:30-10:00
- 联系方式
  - EMail yuchonghu@hust.edu.cn
  - 电话 027-87792450
  - 主页
    - <http://yuchonghu.com>
    - <http://faculty.hust.edu.cn/huyuchong/zh_CN/index.htm>

---

## 授课目标

<style scoped>
  li {
    font-size: 25px;
  }
</style>

- 工程实践方面
  - 熟悉数据中心关键技术平台
    - Kubernetes、OpenStack、Object Storage……
  - 具备运行、维护、使用基础技能
    - Linux, Bash, Vagrant, VirtualBox, Docker……
- 学术探索方面
  - 熟悉相关领域前沿技术与进展
    - 数据中心扩展性、性能、服务质量、可靠性……
  - 锻炼独立研究技能
    - 选题汇报、综述归纳、实验观测和分析数据……

---

## 评分构成

<style scoped>
  li {
    font-size: 20px;
  }
</style>

- **论文研讨** *30%*
  - 制作胶片汇报一篇相关论文，**模拟学术会议**
    - 第一次课内完成 Schedule，确认 12 个 Session Chair 和 48 篇 Paper
    - 每位 Presenter 有 12 分钟汇报和 3 分钟讨论，由 Session Chair 严格组织并计时
    - Session Chair 组织得力可加分
- **综述报告** *30%*
  - 围绕自选研讨主题综述不少于3篇近3年CCF-A/B类会议、期刊论文
    - 内容按计算机学报样式([Doc](http://cjc.ict.ac.cn/wltg/new/submit/CJC-Templet_Word2003.doc), [LaTeX](http://cjc.ict.ac.cn/wltg/new/submit/LatexTemplet.zip))排版后上传仓库文件夹
    - 打印纸质版（A4）
- **考试** *40%*
- 电子版(**汇报胶片、综述报告**)向作业库提交，纸质版只需综述报告，双面打印交国光C523
  - <https://github.com/cs-course/data-center-course-assignment-2022>

---

## 课程计划

<style scoped>
  table {
    width: 100%;
  }
  th {
    background: #003FFF;
  }
  td, p, li {
    font-size: 27px;
  }
</style>

|   | 讲座内容 | 日期 | 地点 |
|:-:|:--------|:---| :--- |
| 1 | [数据中心技术总体介绍](data-center-intro) | 11-03 | D9-D311 |
| 2 | [对象存储技术](object-storage) 及 [存储服务质量保障技术](qos-guarantee) | 11-10 | D9-D311 |
| 3 | 数据中心固态存储技术 (ZNS SSD) | 11-17 | D9-D311 |
| 4 | 数据中心可靠性保障技术 (纠删码) | 11-24 | D9-D311 |
| 5 | 论文研讨* | 12-01 | D9-D311 |
| 6 | 论文研讨 | 12-08 | D9-D311 |
| 7 | 论文研讨 | 12-15 | D9-D311 |
| 8 | 论文研讨 | 12-22 | D9-D311 |

\* *12 presenters in 3 sessions*

---

## 研讨论文列表

![bg right](images/simulated-sessions.png)

扫码在线填表

- 确认 **12 位** 分会主席
- 选择 **48 篇** 拟汇报论文

也可以点击

- [【腾讯文档】数据中心技术课程论文研讨](https://docs.qq.com/doc/DRG1CZFZmaFRRYkJj)

---

## 课堂背景调查

<style scoped>
  p {
    font-size: 20px;
  }
  td {
    font-size: 16px;
    vertical-align:text-top;
    color: #003FFF;
  }
  th {
    display: none;
  }
  table {
    width: 100%;
  }
</style>

扫码进群，参与[调查](https://docs.qq.com/form/page/DRFlyQ2xnaG9xY3Zk?_w_tencentdocx_form=1)，**合计25复选项**

![bg right:32% fit](images/qq-group-2022.jpg)

|||
|:-|:-|
|**动手实践**<br/>- 在裸机上安装过系统<br/>- 自己用零件装配台式机<br/>- 实验室的机群是我配的|**系统环境**<br/>- 只用桌面(GNOME, KDE…)<br/>- 命令行(bash, zsh, fish…)<br/>- 5个以上GNU工具(grep, sed, awk…)<br/>- 远程操作(ssh, tmux, screen…)<br/>- 拥有VPS、云主机|
|**C/C++**<br/>- 作业程序<br/>- 多模块工程(make, autoconf…)<br/>- 知名程序库(STL, Boost, MPI…)|**Java**<br/>- 课程作业<br/>- 构建工具(Ant, Maven, SBT…)<br/>- 知名工程(Hadoop, Spark, Giraph…)|
|**Python**<br/>- 一般脚本<br/>- 管理过系统、运行过网站<br/>- 跑过大数据或ML任务(Tensorflow, torch…)|**还接触过**<br/>- 专业语言(Matlab, R)<br/>- 流行语言(Go, JS, Rust)<br/>- 特长语言(Scala, Julia)|
|**资料来源**<br/>- Stackoverflow<br/>- Github, Bitbucket, Gitee, GitLab<br/>- Linkedin<br/>- LeetCode<br/>- Release Mirrors, Vagrant, Docker…||

---

## 或者扫描问卷条码

![bg right:32% fit](images/qq-group-2022.jpg)

![h:450](images/class-survey.jpg)

---

<style scoped>
  p {
    padding-top: 200px;
    text-align: center;
    font-size: 72px;
  }
</style>

[数据中心技术总体介绍](data-center-intro)
