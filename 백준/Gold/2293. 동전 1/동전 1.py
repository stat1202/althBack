N, K = map(int, input().split())

V = [ int(input()) for _ in range(N)]

prev = [0] * (K + 1)
curr = [0] * (K + 1)

for i in range(K + 1):
  if i % V[0] == 0:
    prev[i] = 1

for i in range(1, N):
  for  j in range(K + 1):
    curr[j] = prev[j]
    if j >= V[i]:
      curr[j] += curr[j - V[i]]
    
  prev = curr

print(prev[K])