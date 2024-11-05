N = int(input())
A = list(map(int, input().split()))

dp = [-1] * N

if len(A) == 1:
  print(0)
else:
  if A[0] != 0:
    dp[0] = 0

  for i in range(N):
    a = A[i]
    for j in range(i, min(i+a + 1, N)):
      # print('dp[i]', dp[i], 'dp[j]', dp[j])
      if dp[j] == -1 and dp[i] != -1:
        dp[j] = dp[i] + 1
      elif dp[j] != -1 and dp[i] != -1: 
        dp[j] = min(dp[j], dp[i] + 1)

  print(dp[N-1])