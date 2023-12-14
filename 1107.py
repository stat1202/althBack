import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
broken = list(map(int, input().rstrip().split() ))

min_count = abs(100 - N)

for nums in range(1000001):
    nums = str(nums)
    
    for i in range(len(nums)):
        if int(nums[i]) in broken:
            break
        elif i == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - N) + len(nums))
print(min_count)
