import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
maze = []
dp = [ [0]*M for _ in range(N)]
for _ in range(N):
    maze.append( list(map(int, input().rstrip().split())) )

for r in range(N):
    for c in range(M):
        n1 = dp[r-1][c-1] if 0<= r-1 < N and 0 <= c-1 < M else 0
        n2 = dp[r][c-1] if 0<= r < N and 0 <= c-1 < M else 0
        n3 = dp[r-1][c] if 0<= r-1 < N and 0 <= c < M else 0
        dp[r][c] = max(n1,n2,n3) + maze[r][c]
        
print(dp[N-1][M-1])