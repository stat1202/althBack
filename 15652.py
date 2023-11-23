import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
l = list(map(str, range(1,N+1)))
for c in combinations_with_replacement(l, M):
    print(" ".join(c))