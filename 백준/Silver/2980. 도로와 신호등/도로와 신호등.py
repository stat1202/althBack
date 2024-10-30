N, L = map(int, input().split())

second = 0
d = 0

for _ in range(N):
  D, R, G = map(int, input().split())
  second += D - d
  d = D

  wait = second % (R+G)
  if wait < R:
    second += R - wait

second += L - d

print(second)