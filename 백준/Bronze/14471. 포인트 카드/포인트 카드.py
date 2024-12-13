N, M = map(int, input().split())

exchange = []
for _ in range(M):
  A, B = map(int, input().split())
  if A >= N:
    M -= 1
  else:
    exchange.append(A)

M -= 1

if M == 0:
  print(0)
else:
  exchange.sort()
  answer = 0
  while M:
    A = exchange.pop()
    answer += N - A
    M -= 1
  print(answer)

