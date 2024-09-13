import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

c_sum = [0] * N
c_sum[0] = A[0]

for i in range(1,N):
  c_sum[i] = c_sum[i-1] + A[i]
answer = 0

count = {}

for i in range(N):
  goal = c_sum[i] - K

  if goal == 0:
    answer += 1

  if goal in count:
    answer += count[goal]

  if c_sum[i] not in count:
    count[c_sum[i]] = 0

  count[c_sum[i]] += 1

print(answer)