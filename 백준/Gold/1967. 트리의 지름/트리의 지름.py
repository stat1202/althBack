from collections import deque

N = int(input())

graph = [[] for _ in range(N)]
scores = [0] * N

for _ in range(N-1):
  s, e, w = map(int, input().split())
  graph[s-1].append((e-1, w))
  graph[e-1].append((s-1, w))


def bfs(start):
  visited = [-1] * N
  q = deque([start])
  visited[start] = 0
  while q:
    v = q.popleft()

    for n, c in graph[v]:
      if visited[n] == -1:
        q.append(n)
        if visited[n] < visited[v] + c:
          visited[n] = max(visited[n],  visited[v] + c )
  dist = max(visited)
  return [visited.index(dist), dist]

answer = bfs(bfs(0)[0])[1]

print(answer)
