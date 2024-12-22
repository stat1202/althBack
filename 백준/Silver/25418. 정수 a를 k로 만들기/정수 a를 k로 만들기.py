from collections import deque
A, K = map(int, input().split())

adj = [ [] for _ in range(K + 1)]

for i in range(1, K + 1):
    if i + 1 <= K:
        adj[i].append(i + 1)
    if 2 * i <= K:
      adj[i].append(2 * i)

visit = [False] * (K + 1)
dist = [-1] * (K + 1)
queue = deque()

queue.append(A)
visit[A] = True
dist[A] = 0

while queue:
  v = queue.popleft()
  for n in adj[v]:
    if not visit[n]:
      queue.append(n)
      visit[n] = True
      dist[n] = dist[v] + 1
print(dist[K])