import sys
input = sys.stdin.readline

N, M = map(int,input().split())

nums = list(map(int,input().split()))

count = 0

left = 0
right = left + 1

while left < N :
  s = sum(nums[left:right])
  if right > N:
    break

  if s < M:
    right += 1
  elif s == M:
    count += 1
    left += 1
    right = left + 1
  else:
    left += 1
    right = left + 1
  
print(count)
    