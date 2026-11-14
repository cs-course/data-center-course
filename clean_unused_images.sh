#!/usr/bin/env bash
# 安全清理「确实作废」的图片。默认只扫描并列清单，绝不删除。
#
# 判定口径（与旧版最大的不同）：
#   只有在「全项目任何文本文件」里，文件名一次都没出现过的图片才算作废。
#   扫描范围包括根目录与 todos/ 等子目录的 *.md、public/*.html、demos/*.html、
#   CSS/JS、*.drawio、*.json 等。因此素材清单文档（只列文件名、不嵌图）登记的
#   照片不会被误判为孤儿 —— 本仓库「未引用 != 无用」。
#
# 用法：
#   bash clean_unused_images.sh                       # dry-run：列清单，不删任何文件
#   bash clean_unused_images.sh --apply              # 列清单 -> 输入 DELETE 确认 -> 备份 -> 分批 git rm
#   bash clean_unused_images.sh --apply --list F     # 用已审阅/编辑过的清单 F（每行一个 images/ 路径）
#   bash clean_unused_images.sh --root-only          # 只处理根仓库，不碰 public/
#   bash clean_unused_images.sh --help
#
# 说明：
#   - public/ 是独立 git 仓库，脚本会分别在两个仓库执行 git rm（只暂存删除，不提交）。
#   - 删除前自动备份到仓库外的 cs-courses-image-backup-<时间戳>/，附 MANIFEST.txt。
#   - 未被 git 跟踪、或有未提交本地改动的文件会被跳过，不会强删。
#   - 清单文件写在仓库外，避免清单自身把待删文件名「登记」进扫描结果。

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)" || exit 1
cd "$ROOT" || exit 1

APPLY=0
ROOT_ONLY=0
LIST_FILE=""

usage() {
    sed -n '2,22p' "$0" | sed 's/^# \{0,1\}//'
}

while [ $# -gt 0 ]; do
    case "$1" in
        --apply)     APPLY=1; shift ;;
        --root-only) ROOT_ONLY=1; shift ;;
        --list)      LIST_FILE="${2:-}"; [ -n "$LIST_FILE" ] || { echo "缺少 --list 的参数" >&2; exit 2; }; shift 2 ;;
        -h|--help)   usage; exit 0 ;;
        *)           echo "未知参数: $1（用 --help 看用法）" >&2; exit 2 ;;
    esac
done

TMP="$(mktemp -d)" || { echo "无法创建临时目录" >&2; exit 1; }
trap 'rm -rf "$TMP"' EXIT

MENTIONED="$TMP/mentioned.txt"   # 在文本源里确实出现过的图片 basename（小写）
NAMES="$TMP/names.txt"           # images/ 下所有图片的 basename
ALL="$TMP/all.txt"               # basename \t path \t size
CAND="$TMP/candidates.tsv"       # 判定作废
LIST="$TMP/list.txt"

# ---------- 1. 列出 images/ 下所有图片 ----------
find images -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \
                       -o -iname '*.gif' -o -iname '*.webp' -o -iname '*.svg' \) -print \
    | while IFS= read -r f; do
        printf '%s\t%s\t%s\n' "$(basename "$f")" "$f" "$(wc -c < "$f" | tr -d ' ')"
      done | sort > "$ALL"
cut -f1 "$ALL" | sort -u > "$NAMES"

# ---------- 2~3. 固定字符串精确匹配（grep -F -f）全项目递归 ----------
# 覆盖所有子目录 md、public/*.html、demos/*.html、CSS/JS、drawio、json 等任意文本文件；
# 文件名含 @ / 空格 / 中文等字符也不会漏判。排除 .git 与 images/ 本身（避免图片自我登记）。
# 不排除 .workbuddy/（宁可多登记、少删除）。清单与备份都写在仓库外，不会参与扫描。
# 若 --list 的清单放在仓库内，额外排除它，避免清单把自己列出的文件名「登记」进去。
EXCLUDE_ARGS=()
[ -z "$LIST_FILE" ] || EXCLUDE_ARGS=(--exclude="$(basename "$LIST_FILE")")
grep -rhoiF --binary-files=without-match -f "$NAMES" \
    --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=bin \
    --exclude-dir=images --exclude-dir=tmp_build \
    ${EXCLUDE_ARGS[@]+"${EXCLUDE_ARGS[@]}"} . 2>/dev/null \
    | tr '[:upper:]' '[:lower:]' | sort -u > "$MENTIONED" || true

# ---------- 4. 差集 = 全项目零提及 ----------
# 用 FILENAME==ARGV[1] 而非 NR==FNR：后者在第一个文件为空时会把第二个文件也误判成第一个
awk -F'\t' 'FILENAME==ARGV[1] { m[$0]=1; next } { k=tolower($1); if (!(k in m)) print $2 "\t" $3 }' \
    "$MENTIONED" "$ALL" > "$CAND"

if [ -n "$LIST_FILE" ]; then
    [ -f "$LIST_FILE" ] || { echo "清单文件不存在: $LIST_FILE" >&2; exit 2; }
    # 允许清单里有空行和 # 注释，方便人工删行/批注
    awk '{ sub(/#.*/, ""); gsub(/^[ \t]+|[ \t]+$/, ""); if ($0 != "") print }' "$LIST_FILE" > "$LIST"
else
    cut -f1 "$CAND" > "$LIST"
fi

# ---------- 5. 报告 ----------
total=$(wc -l < "$ALL" | tr -d ' ')
registered=$(wc -l < "$MENTIONED" | tr -d ' ')
scanned=$(wc -l < "$CAND" | tr -d ' ')
echo "==== 图片清理扫描（$([ "$APPLY" -eq 1 ] && echo 'APPLY 模式' || echo 'DRY-RUN 模式'）) ===="
echo "扫描范围：全项目文本文件（排除 .git / images / bin / node_modules）"
echo "images/ 共 $total 张，其中 $registered 张在文本中出现过；判定作废 $scanned 张"
echo "判定口径：文件名在全部文本文件中零出现（含素材清单登记项）"
[ -z "$LIST_FILE" ] || echo "本次使用指定清单: $LIST_FILE"
echo

n=0
while IFS= read -r f; do
    [ -n "$f" ] || continue
    n=$((n+1))
    rel="${f#images/}"
    pub="无"
    if [ -d public/.git ] && [ -f "public/images/$rel" ]; then
        if [ "$ROOT_ONLY" -eq 0 ]; then
            pub="有（删除前单独校验）"
        else
            pub="有（--root-only 跳过）"
        fi
    fi
    size=$(wc -c < "$f" 2>/dev/null | tr -d ' ')
    printf '%3d. %-58s %8s B   public 副本: %s\n' "$n" "$f" "${size:-?}" "$pub"
done < "$LIST"
echo "清单共 $n 项。"
echo

if [ "$n" -eq 0 ]; then
    echo "没有需要清理的图片，退出（未做任何改动）。"
    exit 0
fi

# 清单写到仓库外，供人工审阅/编辑
REPORT="$ROOT/../cs-courses-unused-images-$(date +%Y%m%d-%H%M%S).txt"
cp "$LIST" "$REPORT"
echo "清单已保存: $REPORT"
echo "  （可删掉不想清理的行，再用 --apply --list <该文件> 执行）"

if [ "$APPLY" -eq 0 ]; then
    echo
    echo "DRY-RUN：以上仅列出，未删除任何文件。确认无误后执行："
    echo "  bash clean_unused_images.sh --apply"
    exit 0
fi

# ---------- 6. 删除前校验：只处理被 git 跟踪且无本地改动的文件 ----------
valid=()
skipped=0
while IFS= read -r f; do
    [ -n "$f" ] || continue
    case "$f" in images/*) ;; *) echo "跳过（路径不在 images/ 下）: $f"; skipped=$((skipped+1)); continue ;; esac
    [ -f "$f" ] || { echo "跳过（文件不存在）: $f"; skipped=$((skipped+1)); continue; }
    git ls-files --error-unmatch -- "$f" >/dev/null 2>&1 || { echo "跳过（未被 git 跟踪）: $f"; skipped=$((skipped+1)); continue; }
    [ -z "$(git status --porcelain -- "$f")" ] || { echo "跳过（有未提交改动）: $f"; skipped=$((skipped+1)); continue; }
    valid+=("$f")
done < "$LIST"

echo
echo "根仓库可安全删除 ${#valid[@]} 张（跳过 $skipped 张）。"
[ "${#valid[@]}" -gt 0 ] || { echo "没有可删除的文件，退出。"; exit 0; }

# public 副本单独登记，只删同样「已跟踪且干净」的
pub_valid=()
if [ "$ROOT_ONLY" -eq 0 ] && [ -d public/.git ]; then
    for f in "${valid[@]}"; do
        [ -f "public/$f" ] || continue
        git -C public ls-files --error-unmatch -- "$f" >/dev/null 2>&1 || { echo "警告：public 副本未被跟踪，跳过: $f"; continue; }
        [ -z "$(git -C public status --porcelain -- "$f")" ] || { echo "警告：public 副本有本地改动，跳过: $f"; continue; }
        pub_valid+=("$f")
    done
    echo "public 仓库可安全删除 ${#pub_valid[@]} 个副本。"
fi

# ---------- 7. 交互确认 ----------
echo
echo "⚠️ 此操作非常危险，可能导致不可逆的数据丢失！"
echo "即将从根仓库 git rm ${#valid[@]} 个文件，从 public 仓库 git rm ${#pub_valid[@]} 个文件（只暂存删除，不提交）。"
printf '确认请输入 DELETE（其它任何输入都取消）：'
if ! IFS= read -r ans; then ans=""; fi
echo
if [ "$ans" != "DELETE" ]; then
    echo
    echo "已取消，未删除任何文件。"
    exit 0
fi

# ---------- 8. 备份 ----------
BAK="$ROOT/../cs-courses-image-backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BAK/repo/images" "$BAK/public/images" || { echo "备份目录创建失败，中止" >&2; exit 1; }
{
    echo "# 图片清理备份  $(date '+%Y-%m-%d %H:%M:%S')"
    echo "# 根仓库 HEAD: $(git rev-parse HEAD 2>/dev/null)"
    echo "# public HEAD: $(git -C public rev-parse HEAD 2>/dev/null)"
    echo "# 恢复: git checkout HEAD -- <path>；public 副本用 git -C public checkout HEAD -- <path>"
    echo "# 格式: 路径 | 字节数 | sha256"
} > "$BAK/MANIFEST.txt"
for f in "${valid[@]}"; do
    cp -p "$f" "$BAK/repo/$f" || { echo "备份失败，中止: $f" >&2; exit 1; }
    printf '%s | %s | %s\n' "$f" "$(wc -c < "$f" | tr -d ' ')" "$(sha256sum "$f" | cut -d' ' -f1)" >> "$BAK/MANIFEST.txt"
done
for f in "${pub_valid[@]}"; do
    cp -p "public/$f" "$BAK/public/$f" || { echo "备份失败，中止: public/$f" >&2; exit 1; }
    printf 'public/%s | %s | %s\n' "$f" "$(wc -c < "public/$f" | tr -d ' ')" "$(sha256sum "public/$f" | cut -d' ' -f1)" >> "$BAK/MANIFEST.txt"
done
echo "备份完成: $BAK （共 $((${#valid[@]} + ${#pub_valid[@]})) 个文件）"

# ---------- 9. 分批删除，每批验证 ----------
BATCH=10
done_n=0
for ((i=0; i<${#valid[@]}; i+=BATCH)); do
    batch=("${valid[@]:i:BATCH}")
    git rm -- "${batch[@]}" || { echo "git rm 失败，立即停止（已删除 $((done_n)) 个）" >&2; exit 1; }
    for f in "${batch[@]}"; do
        [ ! -e "$f" ] || { echo "文件仍存在，立即停止: $f" >&2; exit 1; }
    done
    pbatch=()
    for f in "${batch[@]}"; do
        for p in "${pub_valid[@]}"; do
            [ "$f" = "$p" ] && pbatch+=("$f")
        done
    done
    if [ "${#pbatch[@]}" -gt 0 ]; then
        git -C public rm -- "${pbatch[@]}" || { echo "public git rm 失败，立即停止" >&2; exit 1; }
        for f in "${pbatch[@]}"; do
            [ ! -e "public/$f" ] || { echo "public 文件仍存在，立即停止: $f" >&2; exit 1; }
        done
    fi
    done_n=$((done_n + ${#batch[@]}))
    echo "  第 $((i/BATCH+1)) 批：${#batch[@]} 张（public 副本 ${#pbatch[@]} 个）已删除并验证"
done

echo
echo "完成：根仓库删除 ${#valid[@]} 个、public 仓库删除 ${#pub_valid[@]} 个（均为已暂存未提交状态）。"
echo "备份与恢复说明见: $BAK/MANIFEST.txt"
