from itertools import permutations
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split() )

nums = list(map(int, input().rstrip().split() ))
nums.sort()

for p in sorted(set(permutations(nums, M)) ):
    print(*p)