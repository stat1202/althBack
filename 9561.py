dp = [1,1,1,2,2,3,4,5,7,9] + [0] * 90

for i in range(10,100):
    dp[i] = dp[i-1] + dp[i-5]

T = int(input())
for _ in range(T):
    N = int(input())
    print( dp[N-1] )