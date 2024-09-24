from collections import deque

N = int(input())

q = deque([i for i in range(1, N+1)])

while True:
  n = len(q)
  if n == 1:
    break
  for i in range(n):
    if i % 2 == 0:
      q.popleft()
    else:
      q.append(q.popleft())
print(q[0])