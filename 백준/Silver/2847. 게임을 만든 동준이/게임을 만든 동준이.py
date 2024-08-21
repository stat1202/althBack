import sys

input = sys.stdin.readline

N = int(input())
scores = [int(input()) for _ in range(N)]
cnt = 0
while True:
  flag = True
  for i in range(N-1):
    if scores[i] >= scores[i+1]:
      scores[i] -= 1
      cnt += 1
      flag = False
  if flag:
    break

print(cnt)