import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

A = list(map(int, input().split()))

graph = [ [] for _ in range(N)]
visited = [False] * N
cost = 0

for _ in range(M):
  v,w = map(int, input().split())
  graph[v-1].append(w-1)
  graph[w-1].append(v-1)

def bfs(start):
  q = deque([start])
  visited[start] = True
  costs = []

  while q:
    v = q.popleft()
    costs.append( A[v])
    for n in graph[v]:
      if not visited[n]:
        visited[n] = True
        q.append(n)
  return min(costs)

for i in range(N):
  if not visited[i]:
    cost += bfs(i)

if all(visited):
  if cost <= K:
    print(cost)
  else:
    print("Oh no")
else:
  print("Oh no")