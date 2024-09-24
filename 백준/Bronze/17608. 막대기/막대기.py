import sys
input = sys.stdin.readline

N = int(input())

sticks = [int(input()) for _ in range(N)]

h = 0
count = 0
for i in range(N-1, -1, -1):
  if sticks[i] > h:
    count += 1
    h = sticks[i]

print(count)