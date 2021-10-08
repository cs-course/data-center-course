---
marp: true
theme: gaia
title: 数据中心技术
# size: 4:3
---

<!-- _class: lead -->

# 存储服务质量保障问题

**施展**
武汉光电国家研究中心
光电信息存储研究部

<https://shizhan.github.io/>
<https://shi_zhan.gitee.io/>

---

## 内容大纲

<!-- paginate: true -->

- 存储服务质量保障背景
- 资源决策问题
- 经典方法和实践

---

## 多租户共享存储

---

## 不足还是过量

---

## 资源决策问题

---

## 经典方法

---

### 控制论

---

### 多目标优化

---

### 机器学习

---

## 实践环境

- 大数据存储实验课 <https://github.com/cs-course/iot-storage-experiment>
- 对象存储入门实验 <https://github.com/cs-course/obs-tutorial>

---

### 测试方法与指标

---

## 进一步思考：如何精确控制？

---

### 我们的工作

<style scoped>
  li {
    font-size: 25px;
  }
  p {
    font-size: 20px;
    text-align: center;
  }
</style>

- [Storage Sharing Optimization Under Constraints of SLO Compliance and Performance Variability](https://ieeexplore.ieee.org/document/7498602), ToSC 2019.
- [Customizable SLO and Its Near-Precise Enforcement for Storage Bandwidth](https://dl.acm.org/doi/10.1145/2998454), ToS 2017.
- [PSLO: enforcing the Xth percentile latency and throughput SLOs for consolidated VM storage](https://dl.acm.org/doi/10.1145/2901318.2901330), EuroSys 2016.

![h:270](images/PI-Controller.png)

Source: [PID Controllers Explained](https://blog.opticontrols.com/archives/344)

---

## 参考文献

<style scoped>
  li {
    font-size: 25px;
  }
</style>

1. [Decision-Making Approaches for Performance QoS in Distributed Storage Systems: A Survey](https://ieeexplore.ieee.org/document/8618414), TPDS 2019.
2. [Server consolidation techniques in virtualized data centers of cloud environments: A systematic literature review](https://onlinelibrary.wiley.com/doi/abs/10.1002/spe.2582), SPE 2018.
3. [MittOS: Supporting Millisecond Tail Tolerance with Fast Rejecting SLO-Aware OS Interface](https://dl.acm.org/doi/10.1145/3132747.3132774), SOSP 2017
4. [Crystal: software-defined storage for multi-tenant object stores](https://www.usenix.org/conference/fast17/technical-sessions/presentation/gracia-tinedo), FAST 2017
5. [Argon: Performance Insulation for Shared Storage Servers](https://www.usenix.org/legacy/events/fast07/tech/wachs.html), FAST 2007.
6. [Façade: Virtual Storage Devices with Performance Guarantees](https://www.usenix.org/legacy/events/fast03/tech/lumb.html), FAST 2003.
