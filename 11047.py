import sys
input = sys.stdin.readline

N, K = map(int, input().split() )

coins = [ int( input() ) for _ in range(N)]
coins.sort()
answer = 0
while coins:
    cost = coins.pop()
    if cost <= K:
        cnt = K // cost
        answer += cnt
        K -= cnt * cost
        
print(answer)