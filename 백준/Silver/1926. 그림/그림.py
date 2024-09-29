from collections import deque

N, M = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(N)]

visited = [ [False] * M for _ in range(N)]
d = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(start):
  q = deque([start])  
  dim = 1

  while q:
    v = q.popleft()
    visited[v[0]][v[1]] = True
    for i in range(4):
      ny = v[0] + d[i][0]
      nx = v[1] + d[i][1]
      if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 1 and not visited[ny][nx] :
        q.append( (ny, nx) )
        visited[ny][nx] = True
        dim += 1
  return dim

count = 0
max_dim = 0

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1 and not visited[i][j]:      
      dim = bfs( (i,j) )
      count += 1
      max_dim = max(dim, max_dim)
print(count)
print(max_dim)




