# Ubuntu20.04使用cephadm部署单节点Ceph集群

## 准备工作

#### 1. 配置hosts解析

```bash
vim /etc/hosts 
192.168.1.1 host
这里在最后添加自己机器的ip

```

#### 2. 安装基础组件

- 安装 docker/podman (cephadm基于容器运行所有ceph组件)，这里以podman为例：
  ```bash
  . /etc/os-release
  
  echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/ /" | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
  
  curl -L https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/Release.key | sudo apt-key add -
  
  sudo apt-get update
  apt install -y podman
  ```
- 安装时间服务器:
  ```bash
  sudo apt install -y chrony && sudo systemctl enable --now chrony
  ```

#### 3. 配置SSH访问

```bash
# 允许root用户登录
sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

# 重启ssh服务
systemctl restart ssh

# 设置root密码
sudo passwd
```

## 部署步骤

### 1. 安装cephadm (主节点)

```bash
sudo apt install -y cephadm
```

### 2. 引导新集群

```bash
mkdir -p /etc/ceph
cephadm bootstrap --mon-ip 192.168.1.1  (自己机器的ip)
```

该命令执行以下操作：

- 创建monitor和manager daemon
- 生成SSH密钥
- 添加密钥到authorized_keys
- 配置必要文件
- 生成管理密钥


此时已运行的组件：

- ceph-mgr：管理程序
- ceph-monitor：监视器
- ceph-crash：崩溃数据收集
- prometheus：监控组件
- grafana：监控数据展示
- alertmanager：告警组件
- node_exporter：节点数据收集

### 3. 启用CEPH命令

```bash
# 进入命令状态
sudo cephadm shell

# 查看集群状态
ceph -s

# 查看版本
ceph -v

#安装ceph-common，不用进入cephadm shell也可以使用ceph命令
apt install ceph-common

# 查看集群状态
ceph -s
```
### 4. 部署OSD

这里以sdb为例

```bash
#取消磁盘挂载
umount  /dev/sdb 
```

如果有已经用过的磁盘或清理之前ceph使用的磁盘可使用一下脚本（官方文档引用）
```bash
#!/bin/bash
DISK="/dev/sdb"

# Zap the disk to a fresh, usable state (zap-all is important, b/c MBR has to be clean)
sgdisk --zap-all $DISK

# Wipe a large portion of the beginning of the disk to remove more LVM metadata that may be present
dd if=/dev/zero of="$DISK" bs=1M count=100 oflag=direct,dsync

# SSDs may be better cleaned with blkdiscard instead of dd
blkdiscard $DISK

# Inform the OS of partition table changes
partprobe $DISK

```
或者可使用以下命令清理磁盘
```bash
#查看磁盘
lsblk

#创建物理卷，以sdb为例
pvcreate -ff /dev/sdb

Physical volume "/dev/sdb" successfully created.
#之后即可创建osd
```


```bash

# 创建OSD
ceph orch daemon add osd host:/dev/sdb
```

### 5.部署RGW服务
注意，只有在运行ceph -s时，health OK的情况下才能部署RGW服务
```bash
# 创建rgw服务
ceph orch apply rgw myorg us-east-1 --placement="1 host"

#创建用户(可以指定uid、display_name、access_key、secret_key)
radosgw-admin user create --uid="admin" --display-name="admin" --access-key="admin" --secret-key="123456"
#之后就可以通过http://host:80和admin用户来访问对象存储
```



## 常见问题处理

### 出错后完整删除Ceph集群

```bash
#查看fsid
ceph -s
#清除集群
cephadm rm-cluster --force  --fsid <fsid>
#删除服务
systemctl stop ceph.target
systemctl reset-failed

#查看磁盘
lsblk
#清理磁盘
#之前安装过osd的磁盘上会有ceph--6100837c--0117--4b29--9cbf--00c0c6c13994-osd--block--2e5b167a--7416--4d16--8be8--92e0d82af345这样的逻辑卷
dmsetup remove ceph--6100837c--0117--4b29--9cbf--00c0c6c13994-osd--block--2e5b167a--7416--4d16--8be8--92e0d82af345 
#创建物理卷
pvcreate -ff /dev/sdb
#之后即可部署新的OSD
```
