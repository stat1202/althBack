from collections import deque

N, M = map(int, input().split())
B =  [ list(input()) for _ in range(M) ]

visited = [ [False] * N for _ in range(M) ]
d = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(start, nation):
  q = deque([start])
  visited[start[0]][start[1]] = True
  count = 0
  while q:
    v = q.popleft()
    count += 1
    for i in range(4):
      ny = d[i][0] + v[0]
      nx = d[i][1] + v[1]

      if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] and B[ny][nx] == nation:
        visited[ny][nx] = True
        q.append((ny, nx))
    
  return count

white = 0
blue = 0

for i in range(M):
  for j in range(N):
    if not visited[i][j]:
      c = bfs( (i,j), B[i][j] )

      if B[i][j] == 'W':
        white += c*c
      
      if B[i][j] == 'B':
        blue += c*c

print(white, blue)