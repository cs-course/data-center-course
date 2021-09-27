---
marp: true
theme: gaia
title: 数据中心技术
# size: 4:3
---

# 对象存储专题

**施展**
武汉光电国家研究中心
光电信息存储研究部

---

## 内容大纲

- 对象存储背景
- 尾延迟问题
- 经典方法和实践
- 尾延迟预测

---

## 数字世界发展的恒久挑战

{配图}

---

{配图}

---

## 扩展，还是扩展

- 规模
- 种类

---

{配图}

---

## 对象存储系统

---

## SNIA标准化

……

---

## 典型对象存储

---

{配图Ceph}

---

{配图Openstack Swift}

---

{配图Minio}

---

## 尾延迟问题

---

## 经典方法

---

### Hedged Request

---

### Tied Request

---

## 实践环境

- 大数据存储实验课 <https://github.com/cs-course/iot-storage-experiment>
- 对象存储入门实验 <https://github.com/cs-course/obs-tutorial>

---

### 测试工具

---

### 测试指标

---

## 性能预测难题

给系统建立性能模型

- 分析
- 统计

---

## 性能预测难题…

给系统建立性能模型

- 分析——**系统内部复杂性？**
- 统计——**历史数据全面性？**

---

### 我们的工作

<style scoped>
li {
  font-size: 25px;
}
</style>

- Understanding the latency distribution of cloud object storage systems, JPDC 2019.
- Predicting Response Latency Percentiles for Cloud Object Storage Systems, ICPP 2017.

---

## 实验要求

---

## 参考文献

<style scoped>
li {
  font-size: 25px;
}
</style>

1. Tail Latency in Datacenter Networks, MASCOTS 2020.
2. A Black-Box Fork-Join Latency Prediction Model for Data-Intensive Applications, TPDS 2020.
3. The Fast and The Frugal: Tail Latency Aware Provisioning for Coping with Load Variations, WWW 2020.
4. Managing Tail Latency in Datacenter-Scale File Systems Under Production Constraints, EuroSys 2019.
5. Amdahl's Law for Tail Latency, Commun. ACM 2018.
6. The Tail at Scale: How to Predict It?, HotCloud 16.
7. The Tail at Scale, Commun. ACM 2013.
