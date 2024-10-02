from collections import deque
N = int(input())
M = int(input())

graph = [ [] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(N):
  data = list(map(int, input().split()))

  for j in range(len(data)):
    if data[j] == 1:
      graph[i+1].append(j+1)

destination = list(map(int, input().split()))

q = deque([destination[0]])
visited[destination[0]] = True

while q:
  v = q.popleft()
  for n in graph[v]:
    if not visited[n]:
      visited[n] = True
      q.append(n)

flag = True

for d in destination:
  if not visited[d]:
    flag = False

if flag:
  print("YES")
else:
  print("NO")
