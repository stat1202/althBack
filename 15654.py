from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

nums = list(map(int, input().rstrip().split()))
nums.sort()


answer = list(permutations(nums, M))
for a in answer:
    print(*a)