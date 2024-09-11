from collections import deque
N, M = map(int, input().split())

graph = [ [] for _ in range(N)]
answer = 0
min_kevin= 1e9
for _ in range(M):
  s, e = map(int, input().split())
  graph[s-1].append(e-1)
  graph[e-1].append(s-1)

def bfs(start):
  q = deque([start])
  relation = [0] * N
  while q:
    v = q.popleft()

    for n in graph[v]:
      if relation[n] == 0:
        relation[n] += relation[v] + 1
        q.append(n)
  return sum(relation)

for i in range(N):
  kevin = bfs(i)
  if min_kevin > kevin:
    answer = i+1
    min_kevin = kevin

print(answer)