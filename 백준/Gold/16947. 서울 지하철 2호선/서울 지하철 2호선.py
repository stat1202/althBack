from collections import deque

N = int(input())

adj = [[] for _ in range(N)]
for _ in range(N):
  s, e = map(int, input().split())
  s -= 1
  e -= 1
  adj[s].append(e)
  adj[e].append(s)

degree = [len(adj[i]) for i in range(N)]

while True:
  leaf = []
  for i in range(N):
    if degree[i] == 1:
      leaf.append(i)
  
  if len(leaf) == 0:
    break

  for u in leaf:
    degree[u] = -1
    for v in adj[u]:
      if degree[v] != -1:
        degree[v] -= 1

visit = [False] * N
dist = [-1] * N
queue = deque()

for i in range(N):
  if degree[i] != -1:
    queue.append(i)
    visit[i] = True
    dist[i] = 0

while queue:
  u = queue.popleft()

  for v in adj[u]:
    if not visit[v]:
      visit[v] = True
      dist[v] = dist[u] + 1
      queue.append(v) 
print(*dist)