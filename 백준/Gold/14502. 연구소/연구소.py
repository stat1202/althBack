from itertools import combinations
from collections import deque

N, M = map(int, input().split())
B = [ [] for _ in range(N)]

for i in range(N):
  B[i] = list(map(int, input().split()))

cells = [ (i,j) for i in range(N) for j in range(M) if B[i][j] == 0]

max_safe = 0

for comb in combinations(cells,3):
  for r, c in comb:
    B[r][c] = 1
  
  visited = [ [False] * M for _ in range(N) ]
  queue = deque()

  for i in range(N):
    for j in range(M):
      if B[i][j] == 2:
        queue.append( (i,j) )
        visited[i][j] = True
  
  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]

  while queue:
    r, c = queue.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]

      if 0 <= nr < N and  0 <= nc < M and B[nr][nc] != 1 and not visited[nr][nc]:
        queue.append((nr,nc))
        visited[nr][nc] = True
  
  safe = 0

  for i in range(N):
    for j in range(M):
      if B[i][j] == 0 and not visited[i][j]:
        safe += 1
  max_safe = max(max_safe, safe)

  for r, c in comb:
    B[r][c] = 0
print(max_safe)