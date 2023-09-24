import sys
input = sys.stdin.readline
n = int(input())
nums = [0]* 10001

for _ in range(n):
    nums[ int(input()) ] += 1
# print(nums)

for i in range(1,len(nums)) :
    if nums[i] != 0:
        for j in range( nums[i] ):
            print(i)

    