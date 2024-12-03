from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
W = list(map(int, input().split()))
W.sort()

left = 0
right = N-1

answer = 0

while left < right:
  if W[left] + W[right] <= K: 
    answer += 1
    left += 1
    right -= 1
  else:
    right -= 1
    
print(answer)