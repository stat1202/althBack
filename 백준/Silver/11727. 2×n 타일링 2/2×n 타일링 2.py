dp = [0] * 1000
dp[0] = 1
dp[1] = 3
dp[2] = 5

for i in range(3,1000):
    dp[i] = dp[i-1] + dp[i-2] * 2
N = int(input())
print( dp[N-1] % 10007)