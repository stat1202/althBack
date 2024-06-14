N = int(input())

total_profit = [0]*(N+1)
day = []
profit = []

for _ in range(N):
    t, p = map(int, input().split())
    day.append(t)
    profit.append(p)

for i in range(N):
    for j in range(i+day[i], N+1):
        total_profit[j] = max(total_profit[j], total_profit[i] + profit[i])
print(total_profit[-1])