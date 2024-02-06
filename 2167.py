import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [ list(map(int, input().rstrip().split()) ) for _ in range(n) ]

k = int(input())
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + nums[i-1][j-1] - dp[i-1][j-1]
for _ in range(k):
    i,j,x,y = map(int, input().rstrip().split())
    answer = dp[x][y]- (dp[x][j-1] + dp[i-1][y] ) + dp[i-1][j-1]
    print(answer)