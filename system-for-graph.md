---
marp: true
theme: gaia
title: 数据中心技术、计算机系统设计
# size: 4:3
---

# 面向图应用的系统设计

<!-- _class: lead -->

**施展**
武汉光电国家研究中心
光电信息存储研究部

<https://shizhan.github.io/>
<https://shi_zhan.gitee.io/>

---

## 内容大纲

<!-- paginate: true -->

- 经典图应用及算法
- 对系统的挑战
- 对系统设计的影响
- 图应用的发展
- 新的挑战
- 对系统的探索

---

## 经典图应用

<style scoped>
  li {
    font-size: 18px;
  }
  p {
    font-size: 36px;
    text-align: center;
  }
</style>

![h:300](images/shortest-path.jpg) ![h:300](images/pagerank.webp)

最短路径、网页排名

- [Stanford Network Analysis Project](http://snap.stanford.edu/)
- [The Stony Brook Algorithm Repository](https://www.algorist.com/algorist.html)
- [The Network Data Repository with Interactive Graph Analytics and Visualization](https://networkrepository.com/)

---

## 经典图应用及算法

<style scoped>
  li {
    font-size: 18px;
  }
  p {
    font-size: 36px;
    text-align: center;
  }
</style>

![h:300](images/example-sssp-parallel-bfs-in-pregel-l.jpg) ![h:300](images/pagerank-pregel.jpg) ![h:300](images/pagerank-result.jpg)

最短路径、网页排名

- [Malewicz G, Austern M H, Bik A J C et al. **Pregel: A System for Large-Scale Graph Processing**. SIGMOD 2010.](https://dl.acm.org/doi/10.1145/1807167.1807184)

---

## 对系统的挑战

### 经典系统结构回顾

- 并行结构
- 层次存储

### 图应用带来什么问题

- 偏斜性
- 随机性

---

#### 并行结构

<style scoped>
  h4 {
    padding-top: 500px;
  }
  p {
    font-size: 18px;
  }
</style>

![bg fit](images/Massively-parallel-processing.webp)

[Computer Architecture A Quantitative Approach 6th Edition](https://www.elsevier.com/books/computer-architecture/hennessy/978-0-12-811905-1), Chapter 4, 5.

---

#### 层次存储

<style scoped>
  h4 {
    padding-top: 500px;
  }
  p {
    font-size: 18px;
  }
</style>

![bg fit](images/MemoryHierarchy.png)

[Computer Architecture A Quantitative Approach 6th Edition](https://www.elsevier.com/books/computer-architecture/hennessy/978-0-12-811905-1), Chapter 2.

---

#### 偏斜性

<style scoped>
  li {
    font-size: 18px;
  }
</style>

![h:350](images/power-law-internet.jpg) ![h:300](images/power-law-twitter.jpg)

- [Faloutsos M, Faloutsos P, Faloutsos C. On power-law relationships of the Internet topology. SIGCOMM 1999.](https://dl.acm.org/doi/10.1145/316188.316229)
- [Gonzalez J E, Low Y, Gu H et al. PowerGraph: distributed graph-parallel computation on natural graphs. OSDI 2012.](https://www.usenix.org/system/files/conference/osdi12/osdi12-final-167.pdf)

---

#### 随机性

---

## 对系统设计的影响

- 分布式架构
- 分层式架构
- 分布式、分层架构

---

### 分布式架构

<style scoped>
  p {
    font-size: 18px;
  }
</style>

- MapReduce的问题
- 图分区的矛盾

Source: [Shi Z, Li J, Guo P et al. Partitioning dynamic graph asynchronously with distributed FENNEL. Future Generation Computer Systems, 2017.](https://www.sciencedirect.com/science/article/pii/S0167739X1730033X)

---

### 分层式架构

- 外存模式
  - 大块访问的实现
  - 顺序访问的实现
- 布局问题
  - 如何排序

---

## 图应用的发展

- 异常通话侦测
- 动态图存储

---

## 新的挑战

<style scoped>
  p {
    font-size: 18px;
  }
</style>

- 表示学习
- 时空检索

Source: [CS224W: Machine Learning with Graphs(Stanford)](https://www.bilibili.com/video/BV1me411x7Rm)

---

## 对系统的探索

- 尝试修改采样过程，减少冗余样本 FGCS2019
- 用一套理论来准确指导采样过程，最优化样本尺寸 ICDE2021
- APWeb-WAIM2022

---

## 更多参考

- <https://github.com/jbmusso/awesome-graph>
- <https://github.com/Team309/awesome-graph-processing>
