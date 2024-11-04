N = int(input())

dp = [False] * (1001)

dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True

for i in range(5, N+1):
  dp[i] = (not dp[i-1]) | (not dp[i-3]) | (not dp[i-4])


if dp[N]:
  print('SK')
else:
  print('CY')