---
marp: true
theme: gaia
title: 数据中心技术
# size: 4:3
---

# 对象存储系统尾延迟问题

<!-- _class: lead -->

**施展**
武汉光电国家研究中心
光电信息存储研究部

<https://shizhan.github.io/>
<https://shi_zhan.gitee.io/>

---

## 内容大纲

<!-- paginate: true -->

- 对象存储背景
- 典型对象存储系统
- **长尾延迟问题**
- 经典方法和实践
- **预测问题**
- 一些初步的探讨

---

## 对象存储背景

<style scoped>
  h2 {
    padding-top: 200px;
    text-align: center;
    font-size: 72px;
  }
</style>

---

## 数据洪流

<style scoped>
  p {
    font-size: 20px;
    text-align: right;
  }
</style>

![w:1150](images/IDC_DataSphere.png)

Source: <https://www.datanami.com/2018/11/27/global-datasphere-to-hit-175-zettabytes-by-2025-idc-says/>

---

![bg fit](images/idc-datasphere-2020.webp)

---

<style scoped>
  p {
    font-size: 20px;
    text-align: center;
  }
</style>

![h:580](images/what-happens-online-in-60-seconds.png)

Source: <https://www.smartinsights.com/internet-marketing-statistics/happens-online-60-seconds/>

---

## 迫切需要扩展

<style scoped>
  th {
    font-size: 36px;
  }
  tr {
    font-size: 16px;
    vertical-align: bottom;
  }
</style>

|规模|种类|
|:-:|:-:|
|![w:550](images/scaleout-diagram.jpg)|![w:550](images/OSD-Metadata.webp)|
| Source: <http://sancluster.com/scale-out-file-system/>| Source: <http://storagegaga.com/the-future-is-intelligent-objects/>|

---

## 元数据

<style scoped>
  th {
    font-size: 36px;
  }
  tr {
    font-size: 30px;
    vertical-align: bottom;
  }
</style>

|规模|种类|
|:-:|:-:|
|![w:550](images/scaleout-diagram.jpg)|![w:550](images/OSD-Metadata.webp)|
|**检索地址**|**区分内容**|

---

## 对象存储系统的提出

<style scoped>
  p {
    font-size: 25px;
    text-align: right;
  }
</style>

- Object storage originated in the late 1990s:
- Seagate specifications from 1999
  - [Object Based Storage: A Vision](https://www.t10.org/ftp/t10/document.99/99-341r0.pdf)
  - [Object based storage devices: a command set proposal](https://pdfs.semanticscholar.org/bcd1/97cb0f8544b651289dfdb95efd0b1fd70753.pdf)
- [Dr. Garth Gibson](http://www.cs.cmu.edu/~garth/), CMU & [NASD project](https://www.pdl.cmu.edu/NASD/index.shtml)
  - High-bandwidth, Low-latency, Scalable Storage Systems
  - File Server Scaling with Network-Attached Secure Disks (NASD), 1997

![bg opacity:.2](images/Object-Storage.webp)

Source: <https://www.snia.org/educational-library/object-storage-what-how-and-why-2020>

---

## 和传统存储系统的比较

<style scoped>
  p {
    text-align: center;
  }
</style>

![h:450](images/object-vs-traditional.png)
Source: <https://usdc.vn/object-storage-vs-traditional-storage/>

---

### 传统存储系统

<style scoped>
  p {
    text-align: center;
  }
</style>

![h:450](images/Block-Storage-vs-File-Storage.jpg)
Source: <https://www.ibm.com/cloud/learn/object-storage>

---

### 对象、文件、块和归档存储

<style scoped>
  p {
    text-align: center;
  }
  tr {
    font-size: 25px;
  }
</style>

| Object | File | Block | Archive |
|:-|:-|:-|:-|
| Object Storage | NAS | SAN | Tape |
| Videos, photos serving streaming | All kinds of file | Attach to server | The file needs to be saved permanently |
| Read (download) data regularly | Read data regularly, install as a network drive | Run data directly on Storage | Rarely to download |
| High upload / download speed | High upload / download speed | Very High upload / download speed | High upload speed, slow download |
| Use with CDN | Many usage scenarios | Use with server (VM) | Use independently |

Source: <https://usdc.vn/object-storage-vs-traditional-storage/>

---

## 定义

- [What is Object Storage?](https://www.snia.org/education/what-is-object-storage)
  - Object Storage is a method of storing and subsequently retrieving sets of data as collections of single, uniquely identifiable indivisible items or objects. **It applies to any forms of data that can be wrapped up and managed as an object.**
  - Objects are treated as an atomic unit. **There is no structure corresponding to a hierarchy of directories in a file system**; each object is uniquely identified in the system by a unique object identifier.

---

## 特性

- [What is Object Storage?](https://www.snia.org/education/what-is-object-storage)
  - When you create an object on this type of storage, the **entire set of data** is handled and processed without regard to what sub-parts it may have.
  - When reading from object storage, you can **read either the whole object, or ask to read parts of it**.
  - There is often no capability to update to the object or parts of the object; **the entire object is usually required to be re-written**.
  - Most object storage allows for objects to be deleted.

---

## 特性…

- [What is Object Storage?](https://www.snia.org/education/what-is-object-storage)
  - Object storage often supports meta-data.
    - This is data that is part of the object, but that is in addition to the object ID and the data.
    - It is often expressed as an **attribute-value pair**; for instance, an attribute of COLOR in our collection of objects may have the value RED for some objects and BLUE for others.
    - These permit collections of objects, individually addressable by their object ID, **to be searched, filtered and read in groups** without needing to know the specific object IDs.

---

## 标准化

- **Storage Networking Industry Association** - SNIA
  - [Object Storage: What, How and Why, 2020](https://www.snia.org/educational-library/object-storage-what-how-and-why-2020)
    - Object storage, as a definition, can be: A storage system that manages and manipulates data storage as **distinct units**, called objects
  - [CDMI Cloud Storage Standard, 2.0a, 2020](https://www.snia.org/cloud/cdmi)
    - The Cloud Data Management Interface (CDMI) defines the **functional interface** that applications will use to create, retrieve, update and delete data elements from the Cloud.

---

<style scoped>
  p {
    font-size: 18px;
    padding-top: 620px;
  }
</style>

![bg 85%](images/osd-2007.png)

Source: <https://www.snia.org/educational-library/object-based-storage-device-osd-architecture-and-systems-2007>

---

![bg fit](images/OSD-vs-block-based.webp)

---

![bg fit](images/SCSI-Architecture-OSD.webp)

---

![bg fit](images/osd-commands.png)

---

<style scoped>
  p {
    font-size: 18px;
    padding-top: 620px;
  }
</style>

![bg fit](images/Restful-Web-Services.png)

Source: [What are Restful Web Services](https://gocoding.org/what-are-restful-web-services/)

---

### Amazon S3 REST API

<style scoped>
  p {
    font-size: 18px;
    text-align: center;
  }
  li {
    font-size: 25px;
    text-align: left;
  }
</style>

- **GET** on the API's root resource to list all of the Amazon S3 buckets of a caller.
- **GET** on a Folder resource to view a list of all of the objects in an Amazon S3 bucket.
- **PUT** on a Folder resource to add a bucket to Amazon S3.
- **DELETE** on a Folder resource to remove a bucket from Amazon S3.
- **GET** on a Folder/Item resource to view or download an object from an Amazon S3 bucket.
- **PUT** on a Folder/Item resource to upload an object to an Amazon S3 bucket.
- **HEAD** on a Folder/Item resource to get object metadata in an Amazon S3 bucket.
- **DELETE** on a Folder/Item resource to remove an object from an Amazon S3 bucket.

Source: <https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-s3.html>

---

<style scoped>
  li, p {
    font-size: 18px;
  }
</style>

To access the object-based storage system:

- **secret-access-key** and **access-key-id** – private/public pair of keys that you can generate using different tools or sometimes directly on the provider dashboard
- **endpoint** – the web address of the space

```java
const AWS = require("aws-sdk");

const s3 = new AWS.S3({
  endpoint: "provider-space-endpoint",
  secretAccessKey: "my-secret-key",
  accessKeyId: "my-access-key",
});
```

![bg right fit](images/aws_proxy_s3_create_methods_on_folder.png)

- <https://lakefs.io/object-storage/>
- <https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-s3.html>

---

<style scoped>
  p {
    font-size: 20px;
    color: #F0F0F0;
    text-align: right;
  }
</style>

![bg](images/s3-storage-classes.png)

Source: <https://aws.amazon.com/cn/s3/storage-classes/>

---

<style scoped>
  p {
    font-size: 18px;
    text-align: center;
  }
</style>

![h:600](images/S3-decision-flow-chart_1.png)

Source: <https://www.cloudhealthtech.com/blog/aws-cost-optimization-s3-storage-class>

---

## 更进一步的扩展

<style scoped>
  h2 {
    text-align: center;
  }
</style>

![bg](images/active-object-storage.png)

---

### 主动对象存储

<style scoped>
  h2, p {
    text-align: center;
  }
</style>

![bg opacity:.3](images/active-object-storage.png)

![w:300](images/active-object-storage-award.png)
**主动对象海量存储系统及关键技术**

---

### 算存一体化

<style scoped>
  p {
    font-size: 18px;
    padding-top: 520px;
  }
</style>

![bg fit](images/comp-storage-01.png)
![bg fit](images/comp-storage-02.png)

Source: <https://www.snia.org/computationaltwg>, <https://www.snia.org/education/what-is-computational-storage>

---

### 算存一体化…

![bg opacity:.3 fit](images/comp-storage-01.png)
![bg opacity:.3 fit](images/comp-storage-02.png)

- Computational Storage is defined as architectures that provide **Computational Storage Functions (CSF) coupled to storage**, **offloading host processing** or **reducing data movement**.
- These architectures enable improvements in application performance and/or infrastructure efficiency through the integration of compute resources (outside of the traditional compute & memory architecture) either **directly with storage** or **between the host and the storage**.

---

## 典型对象存储系统

<style scoped>
  h2 {
    padding-top: 200px;
    text-align: center;
    font-size: 70px;
  }
</style>

---

- **Amazon S3**: Amazon S3 stores data as objects within resources called “buckets.” AWS S3 offers features like 99.999999999% durability, cross-region replication, event notifications, versioning, encryption, and flexible storage options (redundant and standard).
- **Rackspace Cloud Files**: Cloud Files provides online object storage for files and media. Cloud Files writes each file to three storage disks on separate nodes that have dual power supplies. All traffic between your application and Cloud Files uses SSL to establish a secure, encrypted channel. You can host static websites (for example: blogs, brochure sites, small company sites) entirely from Cloud Files with a global CDN.

---

- **Azure Blob Storage**: For users with large amounts of unstructured data to store in the cloud, Blob storage offers a cost-effective and scalable solution. Every blob is organized into a container with up to a 500 TB storage account capacity limit.
- **Google cloud storage**: Cloud Storage allows you to store data in Google’s cloud. Google Cloud Storage supports individual objects that are terabytes in size. It also supports a large number of buckets per account. Google Cloud Storage provides strong read-after-write consistency for all upload and delete operations. Two types of storage class are available: Standard Storage class and Storage Near line class (with Near Line being MUCH cheaper).

<https://cloudacademy.com/blog/object-storage-block-storage/>

---

- [**阿里云对象存储OSS（Object Storage Service）**](https://www.aliyun.com/product/oss/)是一款海量、安全、低成本、高可靠的云存储服务，提供99.9999999999%(12个9)的数据持久性，99.995%的数据可用性。多种存储类型供选择，全面优化存储成本。
- [**腾讯对象存储（Cloud Object Storage，COS）**](https://cloud.tencent.com/document/product/436)是腾讯云提供的一种存储海量文件的分布式存储服务，具有高扩展性、低成本、可靠安全等优点。通过控制台、API、SDK 和工具等多样化方式，用户可简单、快速地接入 COS，进行多格式文件的上传、下载和管理，实现海量数据存储和管理。
- [**华为对象存储服务（Object Storage Service）**](https://www.huaweicloud.com/product/obs.html)是一款稳定、安全、高效、易用的云存储服务，具备标准Restful API接口，可存储任意数量和形式的非结构化数据。

---

### OpenStack

<style scoped>
  p {
    font-size: 16px;
    text-align: right;
  }
</style>

- OpenStack was created during the first months of 2010. Rackspace wanted to rewrite the infrastructure code running its Cloud servers offering, and considered open sourcing the existing Cloud files code. At the same time, Anso Labs (contracting for NASA) had published beta code for Nova, a Python-based “cloud computing fabric controller”.
- Both efforts converged and formed the base for OpenStack. The first Design Summit was held in Austin, TX on July 13-14, 2010, and the project was officially announced at OSCON in Portland, OR, on July 21st, 2010.

<https://docs.openstack.org/project-team-guide/introduction.html>

---

### OpenStack Swift

- OpenStack Object Storage (swift) is used for **redundant, scalable data storage using clusters of standardized servers** to store petabytes of accessible data.
- Swift uses a distributed architecture with **no central point of control**, providing greater scalability, redundancy, and performance.
- Storage clusters **scale horizontally** by adding new nodes, uses software logic to ensure data replication and distribution across different devices, inexpensive **commodity hard drives and servers**.

---

<style scoped>
  p {
    font-size: 20px;
    text-align: right;
  }
</style>

<https://docs.openstack.org/swift/>
<https://github.com/openstack/swift>
Source: <https://docs.openstack.org/security-guide/object-storage.html>

![bg fit](images/swift_network_diagram-1.png)

---

### Ceph as a research project

<style scoped>
  li {
    font-size: 30px
  }
  p {
    font-size: 20px;
    text-align: right;
  }
</style>

- Ceph was developed at **University of California, Santa Cruz, by Sage Weil** in 2003 as a part of his PhD project.
  - The initial project prototype was the Ceph filesystem, written in approximately 40,000 lines of C++ code, which was made open source in 2006 under LGPL to serve as a reference implementation and research platform.
  - LLNL supported Sage's initial research work.
  - The period from 2003 to 2007 was the research period of Ceph. By this time, its core components were emerging, and the community contribution to the project had begun at pace.

[Learning Ceph, Packt, 2015](https://subscription.packtpub.com/book/virtualization-and-cloud/9781783985623/1)

---

### Ceph

- Ceph uniquely delivers **object, block, and file storage in one unified system**.
- Ceph is highly reliable, easy to manage, and free.
- Ceph delivers extraordinary scalability–thousands of clients accessing petabytes to exabytes of data.
- A Ceph Node leverages **commodity hardware** and intelligent daemons, and a Ceph Storage Cluster accommodates large numbers of nodes, which communicate with each other to **replicate and redistribute data dynamically**.

---

<style scoped>
  p {
    font-size: 20px;
    text-align: right;
  }
</style>

<https://ceph.io/>
<https://github.com/ceph/ceph>
Source: <https://icicimov.github.io/blog/images/CEPH-graphic.png>

![bg fit](images/ceph-graphic.png)

---

<style scoped>
  p {
    padding-top: 620px;
    font-size: 20px;
  }
</style>

![bg fit](images/ceph-stack.png)

Source: [Ceph Documentation » Architecture](https://docs.ceph.com/en/pacific/architecture/)

---

<style scoped>
  p {
    padding-top: 620px;
    font-size: 20px;
  }
</style>

![bg fit](images/cephDiagramm.webp)

Source: [Ceph storage on Ubuntu: An overview](https://ubuntu.com/blog/ceph-storage-on-ubuntu-an-overview)

---

![bg](images/red-hat-ceph-storage.png)

<!-- https://www.sandisk.com/business/datacenter/resources/solution-briefs/red-hat-ceph-storage-on-the-infiniflash-all-flash-storage-platform -->

---

![bg](images/github-object-storage.png)

---

### Minio

- MinIO is a High Performance Object Storage released under GNU Affero General Public License v3.0.
- It is **API compatible with Amazon S3** cloud storage service.
- **Standalone MinIO servers** are best suited for early development and evaluation.
- Certain features such as versioning, object locking, and bucket replication require distributed deploying MinIO with **Erasure Coding**.

---

<style scoped>
  p {
    font-size: 20px;
    text-align: right;
  }
</style>

<https://min.io/>
<http://www.minio.org.cn/>
<https://github.com/minio/minio>

Source: <http://www.minio.org.cn/static/picture/architecture_diagram.svg>

![bg](images/minio_architecture_diagram.svg)

---

## 课堂实践1

- 说明
  - <https://github.com/cs-course/obs-tutorial>
  - <https://gitee.com/shi_zhan/obs-tutorial>
- 内容
  - 认识对象存储系统
    - 快速部署：Minio、mock_s3…
    - 功能特性：RESTful接口
  - 熟悉性能指标：吞吐率、带宽、延迟
    - 观测工具：s3bench、COSbench…

---

## 对象存储系统的问题之一：长尾延迟

<style scoped>
  h2 {
    padding-top: 200px;
    text-align: center;
    font-size: 60px;
  }
</style>

---

![bg right fit](images/the-long-tail.jpg)

**长尾**（The Long Tail）这一概念是由《连线》杂志主编Chris Anderson在2004年10月的“长尾”一文中最早提出，用来描述诸如亚马逊和Netflix之类网站的商业和经济模式。

实际上是统计学中幂律（Power Laws）和帕累托分布（Pareto distributions）特征的一个口语化表达。

---

![bg right fit](images/the-long-tail.jpg)

**规模化业务**中，“**尾部**”产生的总体效益甚至会超过“**头部**”。

- *冷门商品的销售量可以达到总额的半数*
- *自然语言中的中低频词对信息量的贡献*
- ...

---

<style scoped>
  p {
    padding-top: 600px;
    text-align: center;
    font-size: 18px;
    color: 0040FF;
  }
</style>

![bg fit](images/Thelongtailshift.webp)

<https://newmedia.fandom.com/wiki/The_Long_Tail>

---

<style scoped>
  p {
    padding-top: 200px;
    text-align: center;
    font-size: 72px;
    color: 0040FF;
  }
  li {
    padding-top: 270px;
    text-align: center;
    font-size: 18px;
    color: 0040FF;
  }
</style>

"**长尾**"即不起眼事件的积累

![bg opacity:.3 fit](images/Thelongtailshift.webp)

- <https://newmedia.fandom.com/wiki/The_Long_Tail>

---

### 对系统来说……

<style scoped>
  p {
    padding-top: 150px;
    text-align: center;
    font-size: 72px;
    color: 0040FF;
  }
</style>

![bg opacity:.3](images/distributed-storage.png)

系统以规模扩展应对需求增长

---

### 那么代价是……

<style scoped>
  p {
    padding-top: 150px;
    text-align: center;
    font-size: 72px;
    color: 0040FF;
  }
</style>

![bg opacity:.3](images/workload-plot-1.jpg)

![bg opacity:.3](images/workload-plot-2.jpg)

不起眼的事件也在扩展中积累

<!-- https://www.pdl.cmu.edu/Workload/index.shtml -->

---

![bg fit](images/yi-zhuan.jpg)

<!-- https://github.com/kanripo/KR1a0140/ -->

![bg fit](images/who-moved-my-cheese.jpg)

---

![bg fit](images/WYG0047-0179d.png)

![bg fit](images/it-was-nature-for-change.png)

---

### 『不起眼』的事件将一直存在

<style scoped>
  p {
    padding-top: 150px;
    text-align: center;
    font-size: 72px;
    color: 0040FF;
  }
</style>

![bg opacity:.3 brightness:.5 fit](images/WYG0047-0179d.png)

![bg opacity:.3 brightness:.5 fit](images/it-was-nature-for-change.png)

唯一不变的是变化本身

---

### 归纳起来

毫末之变、扩展之鉴

1. 大系统由小组件汇聚而成
2. 汇聚改变的不仅仅是规模
3. 还有伴随组件而来的变化

系统的扩展将同时成为**小概率事件的放大器**！

---

### 实际系统组件异常情况繁复

![h:450](images/Source-of-Latency.png)

---

### 虽然各有预案

![h:450](images/Source-of-Latency-Solutions.png)

---

### 仍然难免短板

<style scoped>
  p {
    font-size: 20px;
    text-align: left;
  }
</style>

![bg right fit](images/law-of-the-minimum.jpg)

- 必受各组件状态的影响
  - 设备故障 **Fail**
  - 性能波动 **Tail**

Source: <https://nutrien-ekonomics.com/latest-fertilizer-research/liebigs-law-of-the-minimum/>

---

### 容错

<style scoped>
  p {
    font-size: 16px;
    text-align: center;
  }
</style>

- 必受各组件状态的影响
  - 设备故障——需要 **Fault-Tolerant** 容错！

![h:350](images/Replication-and-Erasure-Coding.jpg)

[Cloud Storage Reliability for Big Data Applications: A State of the Art Survey, Journal of Network and Computer Applications 2017](https://linkinghub.elsevier.com/retrieve/pii/S1084804517302734)

---

### 容滞

- 必受各组件状态的影响
  - 设备故障——需要 **Fault-Tolerant** 容错！
  - 性能波动——需要 **Tail-Tolerant** 容滞？

---

![bg fit](images/SNIA-tail-latency.webp)

---

<style scoped>
  p {
    padding-top: 620px;
    font-size: 20px;
  }
</style>

![bg fit](images/latency-sla.png)

Source: <https://bravenewgeek.com/everything-you-know-about-latency-is-wrong/>

---

## 为何要谈尾延迟

- [Everything You Know About Latency Is Wrong](https://bravenewgeek.com/everything-you-know-about-latency-is-wrong/)
- [中译版](https://blog.csdn.net/u012802702/article/details/86421171)
  - **小概率事件**不能忽视

![bg right](images/Screen-Shot-2015-10-04-at-6.15.24-PM-small.jpg)

---

## 为何要谈尾延迟…

- [Everything You Know About Latency Is Wrong](https://bravenewgeek.com/everything-you-know-about-latency-is-wrong/)
- [中译版](https://blog.csdn.net/u012802702/article/details/86421171)
  - **小概率事件**不能忽视
  - 延迟可能"**被平均**"

![bg right fit](images/graph_logbase10_ms.png)

---

## 为何要谈尾延迟……

- [Everything You Know About Latency Is Wrong](https://bravenewgeek.com/everything-you-know-about-latency-is-wrong/)
- [中译版](https://blog.csdn.net/u012802702/article/details/86421171)
  - **小概率事件**不能忽视
  - 延迟可能"**被平均**"
  - 任务可能**被拖累**

![bg right fit](images/web-request-tail.png)

---

## 量化描述尾延迟

<style scoped>
  p {
    font-size: 20px;
    text-align: center;
  }
</style>

![h:500](images/measuring-percentile-latency.svg)

<https://blog.bramp.net/post/2018/01/16/measuring-percentile-latency/>

---

## 规模扩展与尾延迟

<style scoped>
  p {
    font-size: 25px;
  }
</style>

![bg right fit](images/tail-latency-with-scaling-and-outliers.png)

服务器通常响应时间10毫秒，但第P99百分位上的响应时间将达到一秒，即100个请求中将有1个慢请求用时超过1秒。

如果一个用户请求必须并行地从100个这样的服务器收集响应，则63%的用户请求将需要超过一秒的时间（在图表中标记为“x”）。

即使对于请求中只有1/10000（即P9999百分位）超过一秒延迟的服务器，基于2000台这样的服务器的系统也会有近五分之一的用户请求需要超过一秒的时间（在图表中标记为“o”）。

Source：[The Tail at Scale](https://dl.acm.org/doi/10.1145/2408776.2408794), CACM 2013.

<!-- 例如，考虑一个系统，在这个系统中，每个服务器通常的响应时间为10毫秒，但第99百分位的响应时间将达到一秒。如果一个用户请求仅在一个这样的服务器上处理，那么100个用户请求中会有一个请求变慢（一秒）。右图描述了在这种假设情景中，非常小的延迟异常所导致的服务级别延迟的影响。如果一个用户请求必须并行地从100个这样的服务器收集响应，则63%的用户请求将需要超过一秒的时间（在图表中标记为“x”）。即使对于只有万分之一的请求在单个服务器上经历超过一秒延迟的服务，有2,000个这样的服务器的服务也会导致近五分之一的用户请求需要超过一秒的时间（在图表中标记为“o”）。 -->

---

## 如何应对？

- 各组件状态的影响
  - 设备故障——容错——**提供冗余部件** *（回顾计算机系统结构课…）*
  - 性能波动——容滞——？

![h:300](images/3-replica.png) ![h:300](images/erasure-code.png)

---

## 如何应对？…

- 必受各组件状态的影响
  - 设备故障——容错——**提供冗余部件**
  - 性能波动——容滞——**执行冗余操作**

![h:300](images/hedged-requests.png) ![h:200](images/byte-dance-hedged-read.webp)

---

## 经典应对策略

- [SNIA: Avoiding tail latency by failing IO operations on purpose](https://faststorage.eu/snia-avoiding-tail-latency-by-failing-io-operations-on-purpose/)
  - One of these initiatives is adding a per I/O tag that indicates whether a drive **can fail fast** and return an error if it takes too long to retrieve the data.
  - If there’s a replica of the data somewhere else, it might just be faster to retrieve the data from there, instead of waiting for the slow drive to respond.
  - The other side of the coin is a “**try really hard**” I/O tag, that indicates you’ve exhausted all other options and really need the data from this drive.

---

## 主要方法分类

<style scoped>
  li {
    font-size: 25px;
  }
  p {
    font-size: 16px;
    text-align: right;
  }
</style>

- **对冲请求** Hedged Request
  - Issue the same request to multiple replicas and use the results from whichever replica responds first.
  - "hedged" - a client first sends one request to the replica believed to be the most appropriate, but then falls back on sending a secondary request after some brief delay.
  - The client cancels remaining outstanding requests once the first result is received.
- **关联请求** Tied Request
  - The hedged-requests technique also has a window of vulnerability in which multiple servers can execute the same request unnecessarily.
    - Can be capped by waiting for the P95 expected latency before issuing the hedged request, but limits the benefits to only a small fraction of requests.
  - Permitting more aggressive use of hedged requests with moderate resource consumption requires faster cancellation of requests.

[The Tail at Scale](https://dl.acm.org/doi/10.1145/2408776.2408794), CACM 2013.

---

### 案例1：HDFS

<style scoped>
  p {
    font-size: 16px;
    text-align: right;
  }
</style>

- **HDFS** (2.4+)
  - If a read from a block is slow, start up another parallel, **'hedged' read** against a different block replica.
  - We then **take the result of which ever read returns first** (*the outstanding read is cancelled*).
  - This 'hedged' read feature will help rein in the outliers, the odd read that takes a long time because it hit a bad patch on the disc, etc.

<https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/release/2.4.0/RELEASENOTES.2.4.0.html>

---

### 案例2：MongoDB

<style scoped>
  p {
    font-size: 16px;
    text-align: right;
  }
</style>

- **mongodb** (4.4+)
  - With hedged reads, the mongos instances can route read operations to **two replica set members per each queried shard** and **return results from the first respondent** per shard.
  - The additional read sent to hedge the read operation uses the **maxTimeMS** value of **maxTimeMSForHedgedReads**.

<https://docs.mongodb.com/manual/core/read-preference-hedge-option/>

---

### 案例3：字节跳动HDFS改

<style scoped>
  th {
    font-size: 25px;
  }
  td {
    font-size: 25px;
  }
</style>

|Host:X.X.X.X|3 副本Switch Read|2 副本 Hedged Read|3 副本 Hedged Read|3 副本 Fast Switch Read（优化）|
|:-|-:|-:|-:|-:|
|读取时长 p999|977 ms|549 ms|192 ms|128 ms|
|最长读取时间|300 s|125 s|60 s|15.5 s|
|长尾出现次数（大于 500ms）|238 次/天|75 次/天|15 次/天|3 次/天|
|长尾出现次数（大于 1000ms）|196 次/天|64 次/天|6 次/天|3 次/天|

- 优化：根据当前的读取状况动态地调整阈值，动态改变时间窗口的长度以及吞吐量阈值的大小。

[字节跳动 EB 级 HDFS 实践](https://juejin.cn/post/6844904035112189966)

---

## 课堂实践2

- 实验说明
  - <https://github.com/cs-course/obs-tutorial>
  - <https://gitee.com/shi_zhan/obs-tutorial>
- 实验内容
  - 分析不同负载下的指标、延迟的分布
  - 观测尾延迟现象
  - 尝试对冲请求方案

---

## 对象存储系统的问题之二：预测问题

<style scoped>
  h2 {
    padding-top: 200px;
    text-align: center;
    font-size: 60px;
  }
</style>

---

- **容错的代价**
  - …
    - …
    - …
- **容滞的代价**
  - …
    - …
    - …

---

- 容错的代价
  - **浪费的空间**
    - …
    - …
- 容滞的代价
  - **浪费的吞吐**
    - …
    - …

---

- 容错的代价
  - 浪费的空间
    - 从**副本**到**纠删码**、**动态重编码**
    - …
- 容滞的代价
  - 浪费的吞吐
    - **积极对冲**加剧拥塞
    - …

---

- 容错的代价
  - 浪费的空间
    - 从副本到纠删码、动态重编码
    - **故障预测**
- 容滞的代价
  - 浪费的吞吐
    - 积极对冲加剧拥塞
    - **性能预测**

---

### 尾延迟与阿姆达尔定律

<style scoped>
  p {
    font-size: 25px;
  }
</style>

![bg right fit](images/homogeneous-server-queue.jpg)

**尾延迟（也就是最坏情况下的延迟）会使Amdahl's Law变得更重要**：在优化平均性能时，一些部分性能的提升可能不会对整体性能有太大影响，但在优化尾部延迟时，每个部分都可能成为瓶颈。

**队列理论可以提供准确的基础理论**：帮助我们预测和控制系统中的延迟，以指导如何设计未来交互式服务的硬件。

随着服务响应能力和可预测性变得越来越关键，需要根据应用的需求，**找到计算和内存资源之间的平衡**，以实现最优的系统性能。

Source：[Amdahl's Law for Tail Latency](https://dl.acm.org/doi/10.1145/3232559), CACM 2018.

<!-- 首先，优化尾延迟（也就是最坏情况下的延迟）会使Amdahl's Law变得更重要。Amdahl's Law是计算机科学中的一个概念，它描述的是并行计算中加速比的极限。在优化平均性能时，一些部分性能的提升可能不会对整体性能有太大影响，但在优化尾部延迟时，每个部分都可能成为瓶颈，因此需要考虑Amdahl's Law，确保系统的每个部分都得到充分优化。

其次，队列理论可以提供准确的基础理论，以指导如何设计未来交互式服务的硬件。队列理论是研究等待过程（队列）的数学理论，它可以帮助我们预测和控制系统中的延迟。在设计交互式服务的硬件时，我们需要考虑如何减少延迟，提高系统的响应能力，队列理论可以帮助我们实现这一目标。

最后，随着服务响应能力和可预测性变得越来越关键，找到计算和内存资源之间的平衡也变得越来越重要。计算和内存是计算机系统的两个核心资源，它们之间的平衡直接影响到系统的性能。如果计算资源过多，而内存资源不足，那么系统可能会因为内存瓶颈而无法充分发挥计算资源的能力。反之亦然。因此，我们需要根据应用的需求，找到计算和内存资源之间的平衡，以实现最优的系统性能。 -->

---

## 初步尝试——排队论模型

<style scoped>
  li {
    font-size: 25px;
  }
  p {
    text-align: center;
  }
</style>

![h:300](images/Basic-structure-of-queueing-models.png)

- 如何建模**非线性的系统**？
  - [Predicting Response Latency Percentiles for Cloud Object Storage Systems](https://ieeexplore.ieee.org/document/8025298), ICPP 2017.
- 怎么分析**请求的分布**？
  - [Understanding the latency distribution of cloud object storage systems](http://www.sciencedirect.com/science/article/pii/S0743731518301175), JPDC 2019.

---

### 性能模型——考虑要素

![h:500](images/cloud-storage-performance-factors.png)

---

### 性能模型——困难之处

![h:500](images/cloud-storage-performance-prediction.png)

---

### 性能模型——系统分析

![h:500](images/cloud-storage-request-analysis.png)

---

## 更进一步

<style scoped>
  li {
    font-size: 25px;
  }
</style>

- 用预测提高**缓存算法效率**
  - [Fair Will Go On: A Collaboration-Aware Fairness Scheme for NVMe SSD in Cloud Storage System](https://ieeexplore.ieee.org/document/10247718). DAC 2023.
- 用预测改善**服务质量保障**
  - [Graph3PO: A Temporal Graph Data Processing Method for Latency QoS Guarantee in Object Cloud Storage System](https://dl.acm.org/doi/10.1145/3581784.3607075). SC 2023.

---

### 用预测提高**缓存算法效率**

---

### 用预测改善**服务质量保障**

---

## 课堂实践3

- 实验说明
  - <https://github.com/cs-course/obs-tutorial>
  - <https://gitee.com/shi_zhan/obs-tutorial>
- 实验内容
  - 网络存储仿真
  - 排队论模型拟合
  - 思考：准确预测的要素？

---

## 参考文献

<style scoped>
  li {
    font-size: 20px;
  }
</style>

1. [Tail Latency in Datacenter Networks](https://link.springer.com/chapter/10.1007%2F978-3-030-68110-4_17), MASCOTS 2020.
2. [A Black-Box Fork-Join Latency Prediction Model for Data-Intensive Applications](https://ieeexplore.ieee.org/document/9043685), TPDS 2020.
3. [The Fast and The Frugal: Tail Latency Aware Provisioning for Coping with Load Variations](https://dl.acm.org/doi/10.1145/3366423.3380117), WWW 2020.
4. [Managing Tail Latency in Datacenter-Scale File Systems Under Production Constraints](https://dl.acm.org/doi/10.1145/3302424.3303973), EuroSys 2019.
5. [Amdahl's Law for Tail Latency](https://dl.acm.org/doi/10.1145/3232559), CACM 2018.
6. [The Tail at Scale: How to Predict It?](https://www.usenix.org/conference/hotcloud16/workshop-program/presentation/nguyen), HotCloud 16.
7. [The Tail at Scale](https://dl.acm.org/doi/10.1145/2408776.2408794), CACM 2013.
