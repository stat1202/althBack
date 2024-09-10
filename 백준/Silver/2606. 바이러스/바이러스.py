from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
  s, e = map(int, input().split())
  graph[s].append(e)
  graph[e].append(s)

visited = [0] * (N+1)

q = deque([1])
visited[1] = 1

while q:
  v = q.popleft()
  for n in graph[v]:
    if visited[n] == 0:
      q.append(n)
      visited[n] = 1
print(sum(visited) - 1)
