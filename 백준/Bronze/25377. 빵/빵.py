N = int(input())

answer = 1e9
for _ in range(N):
  a, b = map(int, input().split())

  if a <= b:
    answer = min(answer, b)

if answer == 1e9:
  print(-1)
else:
  print(answer)