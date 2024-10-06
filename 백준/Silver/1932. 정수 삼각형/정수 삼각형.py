N = int(input())

A = []
for _ in range(N):
  A.append( list(map(int, input().split())))

dp = [ [0] * i for  i in range(1, N+1)]

dp[0][0] = A[0][0]

for i in range(1, N):
  for j in range(len(dp[i-1])):
    dp[i][j] = max(dp[i][j], dp[i-1][j] + A[i][j])
    dp[i][j+1] = max(dp[i][j+1], dp[i-1][j] + A[i][j+1])

print(max(dp[N-1]))
