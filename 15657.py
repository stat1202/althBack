from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

nums.sort()

for p in combinations_with_replacement(nums, M):
    print(*p)