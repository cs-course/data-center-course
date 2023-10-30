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
2023-10-31 至 2023-12-21

---

## 基本信息

<style scoped>
  li {
    font-size: 30px;
  }
</style>

- 课程资料 <https://github.com/cs-course/data-center-course>  
- 作业库 <https://github.com/cs-course/data-center-course-assignment-2023>
- 参考书
  - [John Hennessy](https://hennessy.stanford.edu/), [David Patterson](https://www2.eecs.berkeley.edu/Faculty/Homepages/patterson.html), [**Computer Architecture: A Quantitative Approach**, 6th Edition.](https://www.elsevier.com/books/computer-architecture/hennessy/978-0-12-811905-1), 2017
  - [**计算机体系结构：量化研究方法**（第6版）](https://item.jd.com/13427803.html), 人民邮电出版社, 2022
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
    - <https://shizhan.github.io/>
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
    - 第一次课内确认计划安排，43位同学每人选择1篇Paper准备汇报
    - 每位同学有**15分钟汇报和3~5分钟讨论**
      - 请严格守时（开PPT排练计时），可自备讲稿辅助（讲台没有分屏模式）
- **综述报告** *40%*
  - 围绕自选研讨主题综述**不少于5篇近3年CCF-A/B类会议、期刊论文**
    - 内容按**计算机学报样式**([Doc](http://cjc.ict.ac.cn/wltg/new/submit/CJC-Templet_Word2003.doc), [LaTeX](http://cjc.ict.ac.cn/wltg/new/submit/LatexTemplet.zip))排版
    - 研讨课中所提的问题和意见需要随文附上**附录：汇报记录**（所提问题，文中相应阐述）
- **汇报胶片、综述报告**课程结束一周内(**2023-12-29**)提交作业库，有特殊情况补充说明可延期一周(**2024-01-05**)提交
  - 作业库：<https://github.com/cs-course/data-center-course-assignment-2023>
- **开卷考试** 30%
  - 综合应用题x3(暂定**2023-12-30**)

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
| 1 | [数据中心技术总体介绍](data-center-intro) | 10-31, 11-02 | D9-D309, D311 |
| 2 | [对象存储技术](object-storage) 及 [存储服务质量保障技术](qos-guarantee) | 11-07, 11-09 | D9-D309, D311 |
| 3 | 数据中心固态存储技术 (ZNS固态盘，童老师) | 11-14, 11-16 | D9-D309, D311 |
| 4 | 数据中心可靠性保障技术 (数据中心纠删码，胡老师) | 11-21, 11-23 | D9-D309, D311 |
| 5 | 论文研讨* | 11-28, 11-30 | D9-D309, D311 |
| 6 | 论文研讨 | 12-05, 12-07 | D9-D309, D311 |
| 7 | 论文研讨 | 12-12, 12-14 | D9-D309, D311 |
| 8 | 论文研讨 | 12-19, 12-21 | D9-D309, D311 |

\* *每周11名同学，每人15分钟报告，3~5分钟问答。*

---

## 研讨论文列表

![bg right](images/reading-list-2023.png)

扫码在线填表

- 每人选择1篇拟汇报论文
- 选择范围：ATC/OSDI23相关论文合计97篇

也可以点击

- [【腾讯文档】数据中心技术课程论文研讨2023](https://docs.qq.com/sheet/DRFF3T0p1b05mcnJO)

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

![bg right:32% fit](images/qq-group-2023.jpg)

|||
|:-|:-|
|**动手实践**<br/>- 在裸机上安装过系统<br/>- 自己用零件装配台式机<br/>- 实验室的机群是我配的|**系统环境**<br/>- 只用桌面(GNOME, KDE…)<br/>- 命令行(bash, zsh, fish…)<br/>- 5个以上GNU工具(grep, sed, awk…)<br/>- 远程操作(ssh, tmux, screen…)<br/>- 拥有VPS、云主机|
|**C/C++**<br/>- 作业程序<br/>- 多模块工程(make, autoconf…)<br/>- 知名程序库(STL, Boost, MPI…)|**Java**<br/>- 课程作业<br/>- 构建工具(Ant, Maven, SBT…)<br/>- 知名工程(Hadoop, Spark, Giraph…)|
|**Python**<br/>- 一般脚本<br/>- 管理过系统、运行过网站<br/>- 跑过大数据或ML任务(Tensorflow, torch…)|**还接触过**<br/>- 专业语言(Matlab, R)<br/>- 流行语言(Go, JS, Rust)<br/>- 特长语言(Scala, Julia)|
|**资料来源**<br/>- Stackoverflow<br/>- Github, Bitbucket, Gitee, GitLab<br/>- Linkedin<br/>- LeetCode<br/>- Release Mirrors, Vagrant, Docker…||

---

## 或者扫描问卷条码

![bg right:32% fit](images/qq-group-2023.jpg)

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
