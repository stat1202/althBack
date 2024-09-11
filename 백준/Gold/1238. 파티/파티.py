import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, M, X = map(int, input().split())
X -= 1

graph = [ [] for _ in range(N) ]
reverse_graph = [ [] for _ in range(N) ]

for _ in range(M):
  s, e, c = map(int, input().split())
  graph[s-1].append((e-1, c))
  reverse_graph[e-1].append((s-1, c))

dist = [1e9] * N
pq = PriorityQueue()
dist[X] = 0
pq.put( (0, X))

while pq.qsize() != 0:
  d, u = pq.get()

  if d != dist[u]:
    continue

  for v, w in graph[u]:
    if dist[v] > dist[u] + w:
      dist[v] = dist[u] + w
      pq.put((dist[v], v))

reverse_dist = [1e9] * N
pq = PriorityQueue()
reverse_dist[X] = 0
pq.put( (0, X))

while pq.qsize() != 0:
  d, u = pq.get()

  if d != reverse_dist[u]:
    continue

  for v, w in reverse_graph[u]:
    if reverse_dist[v] > reverse_dist[u] + w :
      reverse_dist[v] = reverse_dist[u] + w
      pq.put( (reverse_dist[v], v))

max_dist = 0

for i in range(N):
  if max_dist < dist[i] + reverse_dist[i]:
    max_dist = dist[i] + reverse_dist[i]
print(max_dist)