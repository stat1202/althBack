N = int(input())
M = int(input())

D = [ [1e9] * N for _ in range(N)]

for i in range(N):
  for j in range(N):
    if i == j:
      D[i][j] = 0

for _ in range(M):
  a, b, c = map(int, input().split())
  D[a-1][b-1] = min(D[a-1][b-1],c)

for k in range(N):
  for s in range(N):
    for e in range(N):
      D[s][e] = min(D[s][e], D[s][k] + D[k][e])

for i in range(N):
  for j in range(N):
      if D[i][j] == 1e9:
        D[i][j] = 0

for d in D:
  print(*d)