# 计算机系统结构相关课程胶片

华中科技大学 · 武汉光电国家研究中心 & 计算机学院

---

## 课程清单

本仓库包含三门课程的全部 MARP 源文件、编译脚本与部署工程：

### 1. 面向大一新生的「C语言程序设计」

| 源文件 | 内容 |
|--------|------|
| `c-language-pre` | 课程概览、教师信息、教学大纲、排课表 |
| `c-language-background` | 第1章 概论 |
| `c-language-basics` | 第2章 基本元素 |
| `c-language-stdio` | 第3章 格式化输入与输出 |
| `c-language-branch` | 第4章 流程控制 |
| `c-language-function` | 第5章 函数（蒙特卡罗、递归、汉诺塔） |
| `c-language-compiler` | 第6章 编译预处理（宏、条件编译、assert） |
| `c-language-array` | 第7章 数组（成绩表、排序查找） |
| `c-language-pointer` | 第8章 指针 |
| `c-language-struct` | 第9章 结构与联合（链表） |
| `c-language-file` | 第10章 文件操作 |

### 2. 面向研究生新生的「数据中心技术」

| 源文件 | 内容 |
|--------|------|
| `data-center-pre` | 课程概览、Barroso 仓储级计算机、评分、论文研讨、课程计划 |
| `data-center-intro` | 数据中心简介：历史→经典案例→新基建→AI算力→绿色革命 |
| `object-storage` | 对象存储专题：扩展→长尾→尾延迟→Ceph/RadosGW |
| `qos-guarantee` | 存储服务质量保障：云存储→服务器整合→多租户→资源决策 |
| `big-data-storage-experiment` | 大数据存储实验（对象存储技术实验） |
| `ceph-deployment-simple` | Ceph 单节点部署教程（cephadm） |

### 3. 面向研究生新生的「计算机系统设计」独立讲座

| 源文件 | 内容 |
|--------|------|
| `system-for-graph` | 面向图应用的系统设计：经典图算法→Pregel/GraphX→表示学习→KG+LLM |

---

## 维护指南

### 目录结构

```
cs-course/
├── bin/marp                     # MARP CLI 二进制 (~108MB)
├── compile.sh                   # 编译所有 .md → HTML
├── clean_unused_images.sh       # 清理 images/ 中未被引用的图片
├── images/                      # 幻灯片使用的图片、SVG 图表
│   ├── *.svg / *.png / ...      # 生产图片
│   └── *.drawio                 # drawio 源文件
├── *.md                         # MARP 源文件（本课程核心内容）
├── public/                      # 部署工程（独立 Git 仓库）
│   ├── *.html                   # 编译后的 HTML
│   └── images/                  # 同步的图片
├── .gitignore                   # 忽略 bin/, public/, media/
└── .markdownlint.json           # markdownlint 配置
```

### 编译

```bash
# 将全部 .md 编译为 HTML，输出至 public/
bash compile.sh
```

`compile.sh` 工作流程：
1. `bin/marp *.md` — 调用 MARP CLI 批量编译
2. `mkdir public` — 创建部署目录
3. `mv *.html public` — 移动生成的 HTML
4. `cp -r images public` — 同步图片资源

### 清理未使用图片

修改幻灯片后，若移除了部分图片引用，可运行：

```bash
bash clean_unused_images.sh
```

脚本逻辑：扫描所有 `*.md` 中的图片引用路径 → 与 `images/` 中实际文件对比 → 对未被引用的图片执行 `git rm`。执行前会打印待删除列表。

### 部署

`public/` 是一个独立的 Git 仓库（GitHub Pages 部署）：

```bash
cd public
git add -A
git commit -m "update slides"
git push origin master
```

远程仓库：
| 别名 | 地址 | 用途 |
|------|------|------|
| origin | `github.com:cs-course/data-center-course.git` | 源码主仓库 |
| gitee  | `gitee.com:shi_zhan/data-center-course.git` | 国内镜像 |
| public | `github.com:cs-course/marp-public.git` | Pages 部署仓库 |

---

## 维护检查清单

每学期更新前建议执行：

- [ ] 确认排课信息（日期、教室、节次）
- [ ] 更新课程平台邀请码/链接
- [ ] 更新教师联系方式
- [ ] 更新论文研讨范围（会议年份/列表）
- [ ] 结合最新技术发展更新内容
- [ ] 运行 `clean_unused_images.sh` 清理
- [ ] 运行 `compile.sh` 重新编译
- [ ] 在浏览器中检查 `public/*.html` 渲染效果
- [ ] 提交并推送 `public/` 到 Pages
