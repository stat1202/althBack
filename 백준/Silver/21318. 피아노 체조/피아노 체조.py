import sys
input = sys.stdin.readline

N = int(input())
akbo = list(map(int, input().split()))
Q = int(input())

mistake = [0] * N

for i in range(N-1):
  if akbo[i] > akbo[i+1]:
    mistake[i+1] = mistake[i] + 1
  else:
    mistake[i+1] = mistake[i]
for _ in range(Q):
  x, y = map(int, input().split())
  print( mistake[y-1] - mistake[x-1])
