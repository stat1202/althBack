# 2150
import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges = []
result = 0


for _ in range(e):
    a, b, c = map(int, input().split())

    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 루트 노드가 다르다 -> 사이클이 없다
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
