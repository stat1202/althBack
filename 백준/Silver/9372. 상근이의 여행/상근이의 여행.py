from collections import deque

def bfs(graph, start, N):
  q = deque([start])
  visited = [False] * (N+1)
  visited[start] = True
  cnt = 0  

  while q:
    if visited.count(True) == N:
      return cnt
    
    v = q.popleft()

    for n in graph[v]:
      if not visited[n]:
        q.append(n)
        visited[n] = True
        cnt += 1

T = int(input())
for _ in range(T):
  N, M = map(int, input().split(" "))
  graph = [[] for _ in range(N+1)]

  for _ in range(M):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

  print( bfs(graph, 1, N) )