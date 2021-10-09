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

## 广泛应用的云

![bg](images/cloud-storage.jpg)

---

<style scoped>
  p {
    padding-top: 620px;
    font-size: 18px;
  }
</style>

![bg](images/Cloud-Computing-as-a-Service-Revenue.png)

Source: <https://www.kiwiqa.com/top-6-cloud-computing-trends-impacting-cloud-adoption-in-2020/>

---

<style scoped>
  p {
    padding-top: 620px;
    font-size: 18px;
  }
</style>

![bg](images/Top-Four-Cloud-Infrastructure-Providers.jpg)

Source: <https://www.canalys.com/newsroom/worldwide-cloud-market-q320>

---

<style scoped>
  p {
    font-size: 72px;
    text-align: center;
    padding: 120px
  }
</style>

![bg opacity:.3](images/Top-Four-Cloud-Infrastructure-Providers.jpg)

Pandemic boosts cloud consumption by a third in Q3 2020

---

<style scoped>
  p {
    padding-top: 620px;
    font-size: 18px;
  }
</style>

![bg fit](images/CIS_Q320.jpg)

Source: <https://www.srgresearch.com/articles/cloud-market-growth-rate-nudges-amazon-and-microsoft-solidify-leadership>

<!-- New data from Synergy Research Group shows that Q3 enterprise spending on cloud infrastructure services were almost $33 billion, up 33% from the third quarter of 2019. -->

<!-- Amazon and Microsoft continue to account for over half of the worldwide market, with Amazon market share remaining at its long-standing mark of around 33%, while Microsoft’s share was over 18%. Google, Alibaba and Tencent are all growing more rapidly than the overall market and are gaining market share. -->

---

<style scoped>
  p {
    padding-top: 620px;
    font-size: 14px;
  }
</style>

![bg](images/multitenancy-web.png)

Source: <https://www.getfilecloud.com/blog/2014/06/launching-tonido-filecloud-6-0-multi-tenant-amazon-s3-storage-ntfs-permissions-support-and-more/>

---

## 多租户共享存储

---

{QoS场景图}

---

## 服务等级协议

SLA

---

## 服务等级目标

SLO

---

## 不足还是过量

<style scoped>
  p {
    font-size: 18px;
    text-align: left;
  }
</style>

![w:1150](images/provisioning.png)

Source: [A View of Cloud Computing. CACM 2010](https://dl.acm.org/doi/10.1145/1721654.1721672)

---

## 资源决策问题

---

## 评价标准

![h:450](images/slo-spec.png)

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
