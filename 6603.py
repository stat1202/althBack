import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    data = list(map(int, input().rstrip().split()))
    k = data[0]
    if k == 0:
        break
        
    nums = data[1:]
    nums.sort()

    for c in combinations(nums, 6):
        print(*c)
    print()
    