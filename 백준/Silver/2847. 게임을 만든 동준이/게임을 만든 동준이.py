N = int(input())
stages = [int(input()) for _ in range(N)]
cnt = 0
while True:
  flag = True
  for i in range(1,N):
    if stages[i-1] >= stages[i]:
      stages[i-1] -= 1
      cnt += 1
      flag = False
  if flag:
    break
print(cnt)