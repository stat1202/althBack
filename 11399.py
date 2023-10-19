import sys
input = sys.stdin.readline

N = int( input() )
nums = list(map(int, input().rstrip().split() ) ) 

nums.sort(reverse=True)

answer = 0
for i in range(1, N+1):
    answer += nums[i-1] * i
print(answer)