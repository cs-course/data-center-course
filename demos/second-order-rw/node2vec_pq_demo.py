"""
node2vec p/q 可视化演示（课堂演示用，配合 POE 预测环节）

依赖（课前在笔记本上预装，课堂上不再安装）：
    pip install networkx numpy scikit-learn matplotlib gensim

运行：
    python node2vec_pq_demo.py

预期：Karate Club 仅 34 节点，笔记本上 2 分钟内出 3 张图。
演示前先发 POE 预测页（见同目录 poe_page.md），让学生预测 p/q 的影响。

教学要点：
    - p 小 q 大（p<q, BFS 式）→ 偏向"结构等价性"
    - p 大 q 小（p>q, DFS 式）→ 偏向"同质性 (homophily)"
    - 对照预测，讲清 node2vec 二阶转移概率中 p/q 的语义
"""

import time
import networkx as nx
import numpy as np
from sklearn.manifold import TSNE
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def second_order_walk(G, start, p, q, length):
    """node2vec 二阶有偏游走：下一步概率由 (前驱 prev, 当前 cur) 联合状态决定。"""
    walk = [start]
    prev = start
    cur = start
    for _ in range(length):
        neighbors = list(G.neighbors(cur))
        if not neighbors:
            break
        if len(walk) == 1:
            nxt = np.random.choice(neighbors)
        else:
            probs = []
            for nbr in neighbors:
                if nbr == prev:
                    probs.append(1.0 / p)          # d=0
                elif nbr in G.neighbors(prev):
                    probs.append(1.0)              # d=1
                else:
                    probs.append(1.0 / q)          # d=2
            probs = np.array(probs, dtype=float)
            probs /= probs.sum()
            nxt = np.random.choice(neighbors, p=probs)
        walk.append(nxt)
        prev, cur = cur, nxt
    return walk


def generate_walks(G, p, q, num_walks=10, walk_length=20):
    walks = []
    nodes = list(G.nodes())
    for _ in range(num_walks):
        np.random.shuffle(nodes)
        for node in nodes:
            walks.append(second_order_walk(G, node, p, q, walk_length))
    return walks


def embed(walks, dimensions=16, window=4, epochs=20):
    from gensim.models import Word2Vec
    walks_str = [[str(n) for n in w] for w in walks]
    model = Word2Vec(sentences=walks_str, vector_size=dimensions,
                     window=window, min_count=0, sg=1, workers=1, epochs=epochs)
    return model


def run_and_plot(G, p, q, title, outfile):
    t0 = time.time()
    walks = generate_walks(G, p, q)
    model = embed(walks)
    X = np.array([model.wv[str(n)] for n in G.nodes()])
    Y = TSNE(n_components=2, init="pca", random_state=0).fit_transform(X)
    clubs = [G.nodes[n]["club"] for n in G.nodes()]
    plt.figure(figsize=(5, 5))
    cmap = {"Mr. Hi": "#3b6fd4", "Officer": "#e08a2b"}
    for c in set(clubs):
        idx = [i for i, cl in enumerate(clubs) if cl == c]
        plt.scatter(Y[idx, 0], Y[idx, 1], label=c, c=cmap.get(c, "gray"), s=60)
    plt.title(f"{title}\n(p={p}, q={q})")
    plt.legend()
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(outfile, dpi=120)
    plt.close()
    print(f"[{title}] p={p} q={q} 用时 {time.time() - t0:.1f}s -> {outfile}")


def main():
    G = nx.karate_club_graph()
    run_and_plot(G, 1.0, 1.0, "平衡 (p=q=1)", "karate_balanced.png")
    run_and_plot(G, 2.0, 0.5, "偏同质性 (DFS, p>q)", "karate_homophily.png")
    run_and_plot(G, 0.5, 2.0, "偏结构等价 (BFS, p<q)", "karate_structural.png")
    print("\n演示完成：对比三张图——")
    print("  预测：哪种 p/q 让同一俱乐部(Mr. Hi / Officer)的节点更聚拢（同质性）？")


if __name__ == "__main__":
    main()
