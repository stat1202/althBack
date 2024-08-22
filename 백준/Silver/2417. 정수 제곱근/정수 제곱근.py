import sys
input = sys.stdin.readline


n = int(input())

low = 0
high = 2 ** 32
answer = -1
while low <= high:
  mid = (low + high) // 2

  if mid ** 2 < n:
    low = mid + 1
  else:
    answer = mid
    high = mid - 1

print(answer)
