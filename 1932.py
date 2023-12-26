n = int(input())

triangle = []
dp = [ [0]*i  for i in range(1, n+1)]
for _ in range(n):
    data = list(map(int,input().split()))
    triangle.append(data)

dp[0][0] = triangle[0][0]
for i in range(n-1):
    for j in range(i+1):
        # print(i,j)
        dp[i+1][j] = max(triangle[i+1][j] + dp[i][j], dp[i+1][j] )
        dp[i+1][j+1] = max(triangle[i+1][j+1] + dp[i][j], dp[i+1][j+1] )
print(max(dp[-1]))