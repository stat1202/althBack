import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().rstrip().split() ) )

sorted_nums = sorted(list( set(nums) ) )

answer = {}

for i in range(len(sorted_nums)):
    answer[sorted_nums[i]] = i

for i in nums:
    print(answer[i], end = " ")