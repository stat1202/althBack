N, M = map(int, input().split())

answer = 1

if(N >= M):
  answer = 0
else:
  for i in range(N, 0, -1):
    answer *= i
    answer %= M

    if answer == 0:
      break
    
print(answer)