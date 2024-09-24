N, X = map(int, input().split())

answer = -1

for _ in range(N):
  s, t = map(int, input().split())

  if s + t <= X:
    answer = max(answer, s)

print(answer)