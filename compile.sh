#!/bin/bash

# 1. 遇到错误立即停止，防止产物不完整
set -e

echo "🚀 [Build Start] 开始构建项目..."

# --- 配置区域 ---
SRC_IMG_DIR="images"           # 源图片目录
DEST_IMG_DIR="public/images"   # 目标图片目录
BUILD_TMP="tmp_build"          # 临时构建目录
# ---------------

# 2. 清理并准备临时构建目录
echo "🧹 [Cleanup] 正在准备临时构建环境..."
rm -rf "$BUILD_TMP"
mkdir -p "$BUILD_TMP"

# 3. 执行 MARP 编译
echo "📦 正在编译 MARP 幻灯片..."
# 在当前目录执行编译
bin/marp *.md

# 将当前目录下新生成的 html 移动到临时目录中
# 这样可以确保 public 目录的重建是基于最新的编译结果
mkdir -p "$BUILD_TMP"
find . -maxdepth 1 -name "*.html" -exec mv {} "$BUILD_TMP/" \;

# 4. 在临时目录中同步图片资源
echo "🖼️  正在同步图片资源..."
mkdir -p "$BUILD_TMP/images"
rsync -av --delete "$SRC_IMG_DIR/" "$BUILD_TMP/images/"

# 5. 【核心步骤】将临时目录同步到 public，并保护 Git 元数据
echo "🔄 [Sync] 正在同步到发布目录 (保护 Git 元数据)..."

# 确保目标目录存在
mkdir -p public

# 使用 rsync 的 --exclude 功能实现“完美同步”：
# --delete: 确保 public 中不再需要的“僵尸 HTML”被彻底删除
# --exclude='.git': 绝对保护 .git 目录不被删除，确保 git push 功能正常
# --exclude='.github': 保护 GitHub Actions 配置文件
rsync -av --delete \
    --exclude='.git' \
    --exclude='.github' \
    "$BUILD_TMP/" public/

# 6. 清理临时目录
rm -rf "$BUILD_TMP"

echo "✨ [Build Success] 构建与资源同步全部完成！"
echo "✅ 状态：已清理旧 HTML，已同步新图片，已保护 .git 元数据。"
echo "📂 产物目录: $(pwd)/public"
