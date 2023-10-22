import sys
input = sys.stdin.readline

N = int(input () )
steps = [ int(input() ) for _ in range(N) ]
dp = [0]*(N+1)
print(steps)

dp[0] = steps[0]

# [10, 20, 15, 25, 10, 20]
# [10, 0, 0, 0, 0, 0]
for _ in range