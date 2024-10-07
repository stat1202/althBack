N, L, D = map(int, input().split())

check = [True] * 5000

start = 0
for i in range(N):
  for j in range(L):
    check[start + j] = False
  
  start += 5 + L

second = 0
while True:
  if not check[second]:
    second += D
  else:
    break

print(second)