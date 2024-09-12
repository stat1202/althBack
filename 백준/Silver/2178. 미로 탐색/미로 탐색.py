from collections import deque

N, M = map(int, input().split())

graph = [ list(map(int, list(input()))) for _ in range(N) ]
moves = [ [0] * M for _ in range(N) ]

d = [ (1,0), (-1,0), (0,1), (0,-1)]

q = deque([ (0,0) ])
graph[0][0] = 0
moves[0][0] = 1
while q:
  v = q.popleft()

  for y,x in d:
    n_y = v[0] + y
    n_x = v[1] + x

    if 0 <= n_y < N and 0 <= n_x < M and graph[n_y][n_x] == 1:
      moves[n_y][n_x] = moves[v[0]][v[1]] + 1
      graph[n_y][n_x] = 0
      q.append( (n_y, n_x) )
      
print(moves[N-1][M-1])