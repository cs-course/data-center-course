---

## 动手前：先预测（POE）

<!-- 给学生 3 分钟，要求写在纸上，不要讨论 -->

1. **预测题 1**：把 p 调小、q 调大（p<q），游走会更像 BFS 还是 DFS？嵌入会偏向**同质性**还是**结构等价性**？
2. **预测题 2**：反过来 p 大、q 小（p>q）呢？
3. **预测题 3**：观察 Karate Club 的 t-SNE 图，哪种 p/q 让同一俱乐部（Mr. Hi / Officer）的节点更聚拢？

> 写完后与同桌交换，再运行 `node2vec_pq_demo.py` 看结果，对照解释。

---

## 演示：node2vec p/q 可视化

```bash
cd demos/second-order-rw
python node2vec_pq_demo.py
```

- 输出三张图：`karate_balanced.png` / `karate_homophily.png` / `karate_structural.png`
- 对照预测：p>q（DFS）→ 同俱乐部更聚拢（同质性）；p<q（BFS）→ 同结构位置更聚拢（结构等价性）
- 结论：二阶转移概率里的 p/q，正是控制"往回走 vs 向外走"的旋钮
