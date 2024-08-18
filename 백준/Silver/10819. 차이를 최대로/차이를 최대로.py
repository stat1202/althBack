from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))

answer = 0
for p in permutations(nums,N):
  tmp = 0
  for i in range(1,N):
    tmp += abs(p[i-1] - p[i])
  answer = max(answer,tmp)

print(answer)