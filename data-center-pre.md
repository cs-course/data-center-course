---
marp: true
theme: gaia
title: 数据中心技术
# size: 4:3
---

<!-- _class: lead -->

# 数据中心技术

**施展，童薇，胡燏翀，谭支鹏**
武汉光电国家研究中心，计算机学院
2024-11-06 至 2024-12-27

---

## 授课教师

- **施展** 副教授，武汉光电国家研究中心，存储部，C523
- 联系方式
  - EMail <zshi@hust.edu.cn>
  - 主页
    - <https://shizhan.github.io/>
    - <http://faculty.hust.edu.cn/shizhan/zh_CN/index.htm>

---

## 授课教师…

- **童薇** 副教授，武汉光电国家研究中心，存储部，C522
- 联系方式
  - EMail <tongwei@hust.edu.cn>
  - 主页
    - <http://faculty.hust.edu.cn/tongwei/zh_CN/index.htm>

---

## 授课教师……

- **胡燏翀** 教授，计算机科学与技术学院，存储所，B518
- 联系方式
  - EMail <yuchonghu@hust.edu.cn>
  - 主页
    - <http://yuchonghu.com>
    - <http://faculty.hust.edu.cn/huyuchong/zh_CN/index.htm>

---

## 授课教师………

- **谭支鹏** 教授，武汉光电国家研究中心，存储部，C525
- 联系方式
  - EMail <tanzhipeng@hust.edu.cn>
  - 主页
    - <http://faculty.hust.edu.cn/tanzhipeng/zh_CN/index.htm>

---

## 基本信息

<!-- paginate: true -->

<style scoped>
  li {
    font-size: 30px;
  }
</style>

- 课程资料 <https://shi_zhan.gitlab.io/cs-courses/data-center-pre>  
- 作业库 <https://github.com/cs-course/data-center-course-assignment-2024>
- 参考书
  - [John Hennessy](https://hennessy.stanford.edu/), [David Patterson](https://www2.eecs.berkeley.edu/Faculty/Homepages/patterson.html), [**Computer Architecture: A Quantitative Approach**, 6th Edition.](https://www.elsevier.com/books/computer-architecture/hennessy/978-0-12-811905-1), 2017
  - [Luiz André Barroso](https://www.barroso.org/), Urs Hölzle, and Parthasarathy Ranganathan, [**The Datacenter as a Computer: Designing Warehouse-Scale Machines**, Third Edition.](https://www.morganclaypool.com/doi/10.2200/S00874ED3V01Y201809CAC046), 2019
  - [**数据中心一体化最佳实践：设计仓储级计算机**（原书第3版）](https://book.douban.com/subject/34950732/), [美] [路易斯·安德烈·巴罗索](https://www.barroso.org/) 著，徐凌杰 译, 2020
  - [计算机系统结构教程（第3版）](http://www.tup.tsinghua.edu.cn/booksCenter/book_09019101.html)， 清华大学出版社，2021

---

## 计算机系统结构拓展

<style scoped>
  li {
    font-size: 30px;
  }
</style>

![bg right fit](images/caqa6e.jpg)

- [**计算机体系结构：量化研究方法**（第6版）](https://item.jd.com/13427803.html), 人民邮电出版社, 2022

![w:270](images/WSC-in-CAQA6e.png)

---

## 仓储级计算机

<style scoped>
  li {
    font-size: 30px;
  }
  p {
    font-size: 25px;
    font-style: italic;
    color: #F07000;
  }
</style>

- [路易斯·安德烈·巴罗索（Luiz André Barroso）](https://www.barroso.org/)![h:33](images/white-flower-icon-5.jpg)，谷歌研究员、ACM会士、AAAS会士，领导着谷歌的工程基础设施工作。
- [Warehouse-scale Computing](https://dl.acm.org/doi/10.1145/1807167.1837133), SIGMOD '10
- [Warehouse-Scale Computing: Entering the Teenage Decade](https://dl.acm.org/doi/10.1145/2000064.2019527), ISCA '11
- [A Brief History of Warehouse-Scale Computing](https://barroso.org/publications/IEEEMicro2021.pdf), 2020 [Eckert-Mauchly Award](https://awards.acm.org/eckert-mauchly)

Before the onset of the current pandemic, some of us may have underappreciated how important computing technology and cloud-based services have become to our society. In this last year, these technologies have allowed many of us to continue to work, to connect with loved ones, and to support each other. I am grateful to all of those at Google and everywhere in our industry who have built such essential technologies, and I am inspired to be working in a field with still so much potential to improve people’s lives.

<!--
计算机体系结构最高奖Eckert-Mauchly奖，上一年奖项还是颁给那位提出强制、容量和冲突缺失，也就是3C缺失的科学家，就是计算机系统结构课本里面的内容，这次的，也要被写进课本里了，就是最新版的计算机系统结构课本

First awarded in 1979, it was named for John Presper Eckert and John William Mauchly, who between 1943 and 1946 collaborated on the design and construction of the first large scale electronic computing machine, known as ENIAC, the Electronic Numerical Integrator and Computer.
-->

---

Barroso was born in Brazil and had a bachelor’s and master’s degree in electrical engineering from the Pontifical Catholic University of Rio de Janeiro.

In the United States, he did a doctorate in computer engineering at the University of Southern California and worked with processors at Compaq and Digital Equipment Corporation. In 2001, he joined Google as a software engineer.

---

According to an article in Wired, Barroso had never designed a datacenter until he received this request from Google. He came up with the concept of “datacenter as a computer”, building data centres with low-cost components, as we know them today.

He comments that **the lack of experience in datacenter design may have been an advantage**, as we questioned almost every aspect of how these facilities were designed. Perhaps the most important thing was having **the opportunity to look at the entire design**, from the cooling towers to the compilers, and this quickly revealed important opportunities for improvement. Barroso’s idea quickly spread throughout Silicon Valley, among the datacenters of other Internet giants.

---

<style scoped>
  li {
    font-size: 30px;
  }
</style>

  Barroso shared three lessons he learnt in the first half of his career:

  1. **Consider the winding road**: Although there are always risks when embarking on somethingnew, the upside of being adventurous in your professional career can be incredibly rewarding.

  2. **Develop respect for the obvious**: Big problems and important issues have one characteristic incommon: they tend to be simple to understand but difficult to solve. They are obvious and deserveattention.

  3. **Even success has an expiry date**: Some of the most intellectual moments in Barrosa’s careercame when he was forced to abandon his original position, in which he had invested significanttime and effort and achieved some success.

---

## 授课目标

<style scoped>
  li {
    font-size: 25px;
  }
</style>

- 工程实践方面
  - 跟踪一线应用**思考方向**
    - 华为（黄大年茶思屋）、腾讯（犀牛鸟）、阿里（AIR）、浪潮……
  - 积累工程基础**动手实践**
    - Linux, Bash, Vagrant, VirtualBox, Docker……
    - Kubernetes、OpenStack、Object Storage……
- 学术探索方面
  - 相关领域**研讨前沿**技术与进展
    - 数据中心扩展性、性能、服务质量、可靠性……
  - 建立独立研究技能**解决问题**
    - 选题汇报、综述归纳、实验观测和分析数据……

---

## 评分构成

<style scoped>
  li {
    font-size: 20px;
  }
</style>

- **论文研讨** *30%*
  - 制作胶片汇报一篇相关论文
    - 第一次课内确认计划安排，39位同学每人选择1篇Paper准备汇报
    - 每位同学有**12分钟汇报和2~3分钟讨论**
      - 请严格守时（开PPT排练计时），可自备讲稿辅助（讲台没有分屏模式）
- **综述报告** *40%*
  - 围绕自选研讨主题综述**不少于5篇近3年CCF-A/B类会议、期刊论文**
    - 内容按**计算机学报样式**([Doc](http://cjc.ict.ac.cn/wltg/new/submit/CJC-Templet_Word2003.doc), [LaTeX](http://cjc.ict.ac.cn/wltg/new/submit/LatexTemplet.zip))排版
    - 研讨课中所提的问题和意见需要随文附上**附录：汇报记录**（所提问题，文中相应阐述）
- **汇报胶片、综述报告**课程结束一周内(**2025-01-03**)提交作业库，有特殊情况补充说明可延期一周(**2025-01-10**)提交
  - 作业库：<https://github.com/cs-course/data-center-course-assignment-2024>
- **开卷考试** 30%
  - TBA
  - 综合应用题x3(**2024-01-10**晚**18:30-21:00**，**西五楼220**)

---

## 课程计划

<style scoped>
  table {
    width: 100%;
  }
  th {
    background: #003F7F;
  }
  td, p, li {
    font-size: 27px;
  }
</style>

|   | 讲座主题 | 日期 | 地点 |
|:-:|:--------|:---| :--- |
| 1 | [数据中心技术概述](data-center-intro) | 11-06(**周三5-6**) 11-08(**周五3-4**) | C12-S204 |
| 2 | [对象存储技术](object-storage) 及 [存储服务质量保障技术](qos-guarantee) | 11-13, 11-15 | C12-S204 |
| 3 | 数据中心可靠性保障技术 (胡老师) | 11-20, 11-22 | C12-S204 |
| 4 | 数据中心固态存储技术 (童老师) | 11-27, 11-29 | C12-S204 |
| 5 | 数据中心磁盘故障预测技术 (谭老师) | 12-04, 12-06 | C12-S204 |
| 6 | 论文研讨* | 12-11, 12-13 | C12-S204 |
| 7 | 论文研讨 | 12-18, 12-20 | C12-S204 |
| 8 | 论文研讨 | 12-25, 12-27 | C12-S204 |

\* *每周13名同学，每人12分钟报告，2~3分钟问答。*

---

## 研讨论文列表

![bg right](images/reading-list-2024.png)

扫码在线填表

- 每人选择1篇拟汇报论文
- 选择范围：CCF-A相关论文

也可以点击

- [【腾讯文档】数据中心技术课程论文研讨2024](https://docs.qq.com/sheet/DRHJZV01EbWhwaHlZ)

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

![bg right:32% fit](images/qq-group-2024.jpg)

|||
|:-|:-|
|**动手实践**<br/>- 在裸机上安装过系统<br/>- 自己用零件装配台式机<br/>- 实验室的机群是我配的|**系统环境**<br/>- 只用桌面(GNOME, KDE…)<br/>- 命令行(bash, zsh, fish…)<br/>- 5个以上GNU工具(grep, sed, awk…)<br/>- 远程操作(ssh, tmux, screen…)<br/>- 拥有VPS、云主机|
|**C/C++**<br/>- 作业程序<br/>- 多模块工程(make, autoconf…)<br/>- 知名程序库(STL, Boost, MPI…)|**Java**<br/>- 课程作业<br/>- 构建工具(Ant, Maven, SBT…)<br/>- 知名工程(Hadoop, Spark, Giraph…)|
|**Python**<br/>- 一般脚本<br/>- 管理过系统、运行过网站<br/>- 跑过大数据或ML任务(Tensorflow, torch…)|**还接触过**<br/>- 专业语言(Matlab, R)<br/>- 流行语言(Go, JS, Rust)<br/>- 特长语言(Scala, Julia)|
|**资料来源**<br/>- Stackoverflow<br/>- Github, Bitbucket, Gitee, GitLab<br/>- Linkedin<br/>- LeetCode<br/>- Release Mirrors, Vagrant, Docker…||

---

## 或者扫描问卷条码

![bg right:32% fit](images/qq-group-2024.jpg)

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
