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
2024-03-19 (第4周周二) 至 2024-04-09 (第7周周二)
18:30~21:50 @ 南一楼116

---

## 授课教师

- **施展** 副教授，武汉光电国家研究中心，存储部，C523
- 课程公务 每周五上午08:30-10:00
- 联系方式
  - EMail <zshi@hust.edu.cn>
  - 电话 027-87792450
  - 主页
    - <https://shizhan.github.io/>
    - <http://faculty.hust.edu.cn/shizhan/zh_CN/index.htm>

---

<!-- paginate: true -->

## 背景调查

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

- **Lab 0** (03-19) **准备**
  - 按照要求建立课堂作业库，完成首次提交
- **Lab 1** (03-26) **搭建**
  - 熟悉实验基本工具环境，搭建对象存储系统
- **Lab 2** (04-02) **使用**
  - 实践对象存储基本功能，编制脚本和程序完成操作
- **Lab 3** (04-09) **分析**
  - 观测对象存储性能指标，尝试分析和应对性能问题

---

### Lab 0 准备作业库

<style scoped>
  li {
    font-size: 30px;
  }
</style>

- 使用**fork功能**将[总作业库](https://github.com/cs-course/bigdata-storage-experiment-assignment-2024)复刻进自己账号中建立自己的作业库
- 使用`git clone`抓取作业库到本地
- 在本地作业库根目录中建立**以自己学号命名**的目录
- 内置包含学生信息的Markdown格式`README.md`作为目录内容说明
- 建立`Lab0`至`Lab3`子目录，分别放各次实验的**脚本、程序、实验记录**
  - **注意1**：大语言模型的时代**不卷八股报告**，还请**忠实记录实验过程**
  - **注意2**：作业库整洁，实验代码、脚本放`assets`，实验记录配图放`figure`，在实验记录中引用(***没有两次实验的观测是一摸一样的***)
- 添加`git add`（空目录可放占位用文件），提交`git commit`（语义清晰的注释），推送`git push`，交作业（向总作业库发起Pull请求）

---

#### 学号目录 README.md 模板

```Markdown
姓名：XXX
班级：xxxx班
学号：XXXXXXXX

# 课程报告简介

……

# 实验内容简介

……
```

---

#### Lab X README.md 模板

```Markdown
# 实验名称

……

# 实验环境

……

# 实验记录

## 实验X-1：……
……

# 实验小结

……
```

---

### Lab 1 搭建对象存储

- [背景知识](object-storage)
- [实验参考](https://github.com/cs-course/obs-tutorial)
- 目标系统
  - [Minio](https://minio.io/)
  - [Ceph](https://ceph.com/)
  - [OpenStack Swift](http://www.openstack.org/software/releases/ocata/components/swift)

---

### Lab 2 实践基本功能

<style scoped>
  table, li {
    font-size: 30px;
  }
</style>

- 在计算机领域中，[create, read, update, and delete (缩写为 CRUD)](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) 是访问持久存储的4项基本操作。

|    Operation     |  SQL   |        HTTP        |
| :--------------  | :----  | :----------------  |
|      Create      | INSERT |     PUT / POST     |
| Read (Retrieve)  | SELECT |        GET         |
| Update (Modify)  | UPDATE | PUT / POST / PATCH |
| Delete (Destroy) | DELETE |       DELETE       |

- 通过典型界面访问在 Lab 1 中搭建的系统，执行上述典型操作
  - 从标配客户端到API编程

---

#### 【扩展探索】应用集成

- 通过部署实际应用来了解对象存储在云环境中的角色
  - 个人云 [Nextcloud](https://github.com/nextcloud), [Seafile](https://www.seafile.com/home/), [zfile](https://github.com/zhaojun1998/zfile)
  - 图片管理 [Thumbor](http://thumbor.org/), [picfit](https://github.com/thoas/picfit)
  - ……

---

### Lab 3 观测分析性能

<style scoped>
  li {
    font-size: 30px;
  }
</style>

实验测试工具

- [s3bench](https://github.com/igneous-systems/s3bench), [benchio](https://github.com/giacomoguiulfo/benchio), [s3-benchmark](https://github.com/chinglinwen/s3-benchmark) (Go语言)
- [s3-bench-rs](https://github.com/SKTT1Ryze/s3-bench-rs) (Rust语言)
  - 感谢 [@SKTT1Ryze](https://github.com/SKTT1Ryze) 同学提供，欢迎更多同学参与！
- [COSBench](https://github.com/intel-cloud/cosbench) (Java语言)

---

#### 观察影响性能的主要因素

<style scoped>
  li {
    font-size: 30px;
  }
</style>

典型问题举例

- 对象尺寸如何影响性能?
  - 对于熟悉的某类应用，根据其数据访问特性，怎样适配对象存储最合适?
- 如何全面观测I/O延迟?
  - 平均值与统计分布
- 如果客户端爆满将怎样?
  - 请求并发数如何同时影响延迟分布和吞吐率？如何保障服务质量？
- 横向扩展系统 (Scaling Out) 效果如何 (向系统中追加更多存储服务器)?

---

#### 【扩展探索】尾延迟问题

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
  - 用LLM工具辅助，如：<https://kimi.moonshot.cn/>

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
| $Server$ | Minio Server | s3proxy/mock-s3/... | Ceph/Swift |
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

在 <https://github.com/cs-course/bigdata-storage-experiment-assignment-2024> 中完成实验记录

周一的**课堂学习也会要求交一份作业**，请上传进作业库中自己的文件夹。

### 提交日期

第9周周二：**2024-04-23**

### 延迟提交

有合理原因请附说明提交作业，可延迟1周至**2024-04-30**，规则参考

1. [cs231n assignments](http://vision.stanford.edu/teaching/cs231n/assignments.html)
2. [EE365: Late Policy](https://stanford.edu/class/ee365/late.html)
3. [Late submission of coursework](https://www.essex.ac.uk/student/exams-and-coursework/late-submission-of-coursework)
4. [What are the penalties for late submission of an assignment?](https://www.sheffield.ac.uk/mltc/courses/learning/validation)
5. [What to Say (and Not Say) When Handing in Late Assignments, According to Professors](https://lifehacker.com/what-to-say-and-not-say-when-handing-in-late-assignme-1850343910)

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
