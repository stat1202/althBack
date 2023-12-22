from itertools import permutations

N = int(input())
nums = [i for i in range(1,N+1)]

for p in permutations(nums):
    print(*p)