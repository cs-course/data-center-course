@echo off

REM 使用 marp 转换所有 .md 文件
bin\marp *.md

REM 创建 public 目录（如果不存在）
if not exist public mkdir public

REM 移动所有 .html 文件到 public 目录
move *.html public

REM 复制 images 目录
xcopy images public\images /E /I /Y