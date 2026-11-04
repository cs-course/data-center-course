#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
论文研讨课选题分配器（保覆盖分配）
==================================
输入：36 个小组的选题意向（每组 1st/2nd/3rd 志愿，论文编号 1..36）
输出：36 组 -> 36 篇 的一一对应分配，且【每篇必有一组】（全覆盖）

核心保证（针对"某篇没人选 / 某篇被抢"导致 session 排期被打乱的问题）：
  - 组数 == 论文数 == 36，做满射双射，故 36 篇每篇恰好一组
  - 优先满足高优先志愿；个别无人选的论文由"志愿满足最差"的组兜底
  - 输出统计 + 冲突报告，便于人工复核

用法：
  python3 assign_papers.py --self-test          # 用模拟数据自测
  python3 assign_papers.py submissions.csv       # 读真实提交（列：group_id,m1,m2,m3,pref1,pref2,pref3）
  python3 assign_papers.py submissions.csv --out result.csv
"""
import argparse, csv, json, random, sys

# ---------- 论文编号 -> 标题（从 dc-tech-seminar-papers.csv 提取） ----------
def load_paper_titles(csv_path):
    titles = {}
    try:
        with open(csv_path, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                try:
                    titles[int(row["编号"].strip())] = row["论文标题"].strip()
                except (KeyError, ValueError):
                    pass
    except FileNotFoundError:
        pass
    return titles

# ---------- 分配核心 ----------
def assign(groups):
    """
    groups: list of dict {id, prefs:[p1,p2,p3] (None 表示未填)}
    返回 (assignment, stats, conflicts)
      assignment: {group_id: paper_no}
    """
    PAPERS = list(range(1, 37))
    owner = {}            # paper_no -> group_id
    assignment = {}       # group_id -> paper_no
    unassigned = list(groups)

    # 三轮：先 1st，再 2nd，再 3rd（按提交顺序/组号，稳定）
    for rank in (0, 1, 2):
        still = []
        for g in unassigned:
            p = g["prefs"][rank]
            if p is None or p not in PAPERS or p in owner:
                still.append(g)
                continue
            owner[p] = g["id"]
            assignment[g["id"]] = p
        unassigned = still

    # 兜底：剩余未分配组 <-> 剩余未分配论文 做双射（保证全覆盖）
    free_papers = [p for p in PAPERS if p not in owner]
    forced = []
    for g in unassigned:
        if not free_papers:
            break
        p = free_papers.pop(0)
        owner[p] = g["id"]
        assignment[g["id"]] = p
        forced.append((g["id"], p))

    # 统计满足度
    sat = {"pref1": 0, "pref2": 0, "pref3": 0, "forced": 0}
    for g in groups:
        got = assignment[g["id"]]
        if got == g["prefs"][0]:
            sat["pref1"] += 1
        elif got == g["prefs"][1]:
            sat["pref2"] += 1
        elif got == g["prefs"][2]:
            sat["pref3"] += 1
        else:
            sat["forced"] += 1

    # 冲突报告：被多组列为同优先级的论文
    conflicts = []
    for p in PAPERS:
        want1 = [g["id"] for g in groups if g["prefs"][0] == p]
        if len(want1) > 1:
            conflicts.append((p, 1, want1))
        want2 = [g["id"] for g in groups if g["prefs"][1] == p]
        if len(want2) > 1:
            conflicts.append((p, 2, want2))

    return assignment, sat, conflicts, forced

# ---------- 模拟自测 ----------
def self_test(trials=200, seed=0):
    random.seed(seed)
    titles = load_paper_titles(r"d:\documents\portforlio\Course\cs-courses\todos\dc-tech-seminar-papers.csv")
    print(f"[自测] 论文标签加载：{len(titles)} 篇")
    worst = {"pref1": 999, "pref2": 999, "pref3": 999, "forced": 999}
    for t in range(trials):
        groups = []
        for i in range(36):
            prefs = random.sample(range(1, 37), 3)  # 随机 3 个不同志愿
            groups.append({"id": f"G{i+1:02d}", "prefs": prefs})
        a, sat, conf, forced = assign(groups)
        # 不变量校验
        assert len(a) == 36, f"trial {t}: 分配数 {len(a)} != 36"
        assert set(a.values()) == set(range(1, 37)), f"trial {t}: 论文未全覆盖 {set(range(1,37)) ^ set(a.values())}"
        assert len(set(a.values())) == 36, f"trial {t}: 论文被重复分配"
        for k in sat:
            worst[k] = min(worst[k], sat[k])
    print(f"[自测] {trials} 次随机分配均通过不变量（36 组->36 篇 双射、全覆盖、无重复）")
    print(f"[自测] 各满足度的最差情况（越低越差）：{worst}")
    # 极端场景：故意让某篇无人选、某篇被 10 组抢
    groups = []
    for i in range(36):
        if i == 0:
            prefs = [7, 8, 9]          # 正常
        elif i < 10:
            prefs = [1, 2, 3]          # 前 9 组都抢论文 1
        else:
            prefs = [i+1 if i+1 <= 36 else 36, None, None]  # 各自选不同，论文 36 可能无人选
        groups.append({"id": f"G{i+1:02d}", "prefs": prefs})
    a, sat, conf, forced = assign(groups)
    print(f"[极端] 满足度={sat}  兜底组数={len(forced)}  冲突(>1组同优先)={len(conf)}")
    print(f"[极端] 论文36 分配给了: {[k for k,v in a.items() if v==36]}  (应非空，证明兜底生效)")
    print("[自测] 通过。")

# ---------- 真实提交 ----------
def read_submissions(path):
    groups = []
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            def num(x):
                x = (x or "").strip()
                return int(x) if x.isdigit() and 1 <= int(x) <= 36 else None
            prefs = [num(row.get(f"pref{n}")) for n in (1, 2, 3)]
            groups.append({"id": row.get("group_id", "").strip() or f"G{len(groups)+1:02d}",
                           "prefs": prefs,
                           "members": [row.get(f"m{i}", "").strip() for i in (1, 2, 3) if row.get(f"m{i}", "").strip()]})
    if len(groups) != 36:
        print(f"⚠️ 提交组数为 {len(groups)}，不等于 36！请先按 28×2+8×3 调平后再分配。", file=sys.stderr)
    return groups

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?", help="提交意向 CSV")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--out", default="assignment_result.csv")
    args = ap.parse_args()

    if args.self_test or not args.csv:
        self_test()
        return

    titles = load_paper_titles(r"d:\documents\portforlio\Course\cs-courses\todos\dc-tech-seminar-papers.csv")
    groups = read_submissions(args.csv)
    a, sat, conf, forced = assign(groups)

    with open(args.out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["group_id", "组员学号", "分配论文编号", "论文标题", "满足度", "会议"])
        for g in groups:
            p = a[g["id"]]
            deg = "forced" if g["id"] in [x[0] for x in forced] else (
                "pref1" if p == g["prefs"][0] else "pref2" if p == g["prefs"][1] else "pref3")
            conf_csv = r"d:\documents\portforlio\Course\cs-courses\todos\dc-tech-seminar-papers.csv"
            # 取会议：简单从 titles 无法拿到，单独读
            w.writerow([g["id"], " / ".join(g["members"]), p, titles.get(p, ""), deg, ""])
    print(f"✅ 分配完成，已写入 {args.out}")
    print(f"   满足度：{sat}")
    print(f"   冲突(同优先>1组)：{len(conf)} 篇；兜底组：{len(forced)}")
    if conf:
        for p, r, gs in conf:
            print(f"     论文{p} 被 {len(gs)} 组列为第{r}志愿：{gs}")

if __name__ == "__main__":
    main()
