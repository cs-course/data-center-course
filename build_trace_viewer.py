import json, re, io

BASE = r'd:/documents/portforlio/Course/computer-architecture/lab/computer-architecture-experiment/data/cachelab-handout/'
TEMPLATE = r'd:/documents/portforlio/Course/cs-courses/demos/graph-trace-viewer-template.html'
OUT = r'd:/documents/portforlio/Course/cs-courses/demos/graph-trace-viewer.html'

specs = [
    ('bfs-128-csr',     '原始顺序布局', '#4fc3f7'),
    ('bfs-128-dd-csr',  '度降序布局 DD', '#ffb74d'),
    ('bfs-128-bfs-csr', 'BFS 遍历序布局', '#81c784'),
]

traces = []
total_repaired = 0
for stem, label, color in specs:
    xl = json.load(open(r'd:/documents/portforlio/Course/cs-courses/traces.json'))[stem]
    csv = [l.strip().split(',') for l in open(BASE + stem + '.csv') if l.strip()]
    assert len(xl) == len(csv), (stem, len(xl), len(csv))
    repaired = 0
    data = []
    for (op, hx, size, dec), (cop, caddr, csize) in zip(xl, csv):
        a = int(caddr, 16)          # CSV = authoritative raw trace
        if a != dec:
            repaired += 1
        assert cop == op and int(csize) == size
        data.append([0 if op == 'L' else 1, a, size])
    traces.append({'label': label, 'stem': stem, 'color': color,
                   'repaired': repaired, 'data': data})
    total_repaired += repaired
    print(stem, 'rows', len(data), 'repaired', repaired)

html = open(TEMPLATE, encoding='utf-8').read()
payload = json.dumps(traces, separators=(',', ':'), ensure_ascii=False)
html = html.replace('/*__DATA__*/[]', payload, 1)
open(OUT, 'w', encoding='utf-8').write(html)
print('total repaired', total_repaired, '-> wrote', OUT, len(html), 'bytes')
