---
marp: true
theme: gaia
title: 数据中心技术
# size: 4:3
---

# 数据中心技术

**施展，童薇**
武汉光电国家研究中心
2021-11-12 至 2021-12-31

---

## 基本信息

- 课程资料 <https://github.com/cs-course/data-center-course>  
- 作业库 <https://github.com/cs-course/data-center-course-assignment-2021>
- 参考书
  - 云计算——概念、技术与架构，机械工业出版社，2014
  - Luiz André Barroso, Urs Hölzle, and Parthasarathy Ranganathan, **The Datacenter as a Computer: Designing Warehouse-Scale Machines**, Third Edition., 2019
    - <https://www.morganclaypool.com/doi/10.2200/S00874ED3V01Y201809CAC046>

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

## 授课目标

<!-- Scoped style -->
<style scoped>
li {
  font-size: 25px;
}
</style>

- 工程实践方面
  - 能初步完成数据中心实际部署
    - Kubernetes (k8s)、OpenStack
  - 具备运行、维护、使用基础技能
    - Linux, Bash, Object Storage, Vagrant, VirtualBox, Docker
- 学术探索方面
  - 熟悉相关领域前沿技术与进展
    - 虚拟化、对象存储、监控管理……
  - 能独立开展相关领域创新性研究
    - 监控管理、调度迁移、应用、可靠、节能、安全……

---

## 授课目标…

<!-- Scoped style -->
<style scoped>
li {
  font-size: 25px;
}
</style>

- 评分构成
  - 综述报告 *30%*
    - 围绕一项主题综述不少于3篇近3年CCF-A/B类会议、期刊论文
    - 篇幅10至15页（A4），样式参考计算机学报
  - 论文研讨 *30%*
    - PPT汇报上述报告内容，(15分钟汇报+5至10分钟讨论)/人
    - 高质量提问加分
  - 实验 *40%*
    - k3s-lab 20%, obs-lab 20%
    - QQ群实名接龙确认完成，研讨课余集中检查
- 电子版向作业库提交，纸质版双面打印交国光F307

---

## 课程计划

<!-- Scoped style -->
<style scoped>
td {
  font-size: 30px;
}
</style>

|   | 讲座内容 | 日期 | 地点 |
|:-:|:--------|:---| :--- |
| 1 | 数据中心技术总体介绍 | 11-12 | 南一楼116机房 |
| 2 | 数据缩减技术 | 11-19 | 南一楼116机房 |
| 3 | 对象存储技术 | 11-26 | 南一楼116机房 |
| 4 | 课堂实验1：lab1 | 12-03 | 南一楼116机房 |
| 5 | 课堂实验2：lab2 | 12-10 | 南一楼116机房 |
| 6 | 论文研讨 | 12-17 | 南一楼116机房 |
| 7 | 论文研讨 | 12-24 | 南一楼116机房 |
| 8 | 论文研讨 | 12-31 | 南一楼116机房 |

---

## 后续内容

- 数据中心的背景知识
