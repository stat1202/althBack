from itertools import combinations
import sys
input = sys.stdin.readline
N, S = map(int,input().split())
seq = list(map(int,input().split()))

count = 0

for n in range(1, N+1):
  for combination in combinations(seq, n):
    if sum(combination) == S:
      count += 1

print(count)