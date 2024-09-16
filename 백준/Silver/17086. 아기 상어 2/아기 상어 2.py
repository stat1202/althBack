from collections import deque
N, M = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(N) ] 
dist = [ [-1] * M for _ in range(N) ]

q = deque()
d = [(1,0), (-1,0), (0, 1), (0, -1), (1,1), (1,-1), (-1,1), (-1,-1)]

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      q.append( (i, j) )
      dist[i][j] = 0

while q:
  v = q.popleft()
  graph[v[0]][v[1]] = 1
  
  for i in range(8):
    ny = d[i][0] + v[0]
    nx = d[i][1] + v[1]

    if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
      q.append( (ny, nx) )
      dist[ny][nx] = dist[v[0]][v[1]] + 1
      graph[ny][nx] = 1

print( max(sum(dist, [])) )

