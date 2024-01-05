import sys
input = sys.stdin.readline

N = int(input())

init = list(map(int, input().rstrip().split()))

max_dp = [0] * 3
min_dp = [0] * 3
for i in range(3):
    max_dp[i] = init[i]
    min_dp[i] = init[i]

for i in range(1, N):
    
    scores = list(map(int, input().rstrip().split()))
    
    max_0 = max(max_dp[0], max_dp[1] ) + scores[0]
    max_1 = max(max_dp[0], max_dp[1], max_dp[2] ) + scores[1]
    max_2 = max(max_dp[1], max_dp[2] ) + scores[2]
    
    max_dp[0] = max_0
    max_dp[1] = max_1
    max_dp[2] = max_2
    
    
    min_0 = min(min_dp[0], min_dp[1] ) + scores[0]
    min_1 = min(min_dp[0], min_dp[1], min_dp[2] ) + scores[1]
    min_2 = min(min_dp[1], min_dp[2] ) + scores[2]
    
    min_dp[0] = min_0
    min_dp[1] = min_1
    min_dp[2] = min_2
print( max(max_dp), min(min_dp) )
