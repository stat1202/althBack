# N 유저 수 M 친구 관계 수
from collections import deque

N,M = map(int, input().split() )

graph = [ [] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split() )
    graph[start].append(end)
    graph[end].append(start)
# print(graph)
answer = []
def bfs(graph, node, visited):
    num = [0] * (N+1)
    queue = deque([node])
    path = []

    visited[node] = True

    while queue:
        v = queue.popleft()
        path.append(v)       
        for i in graph[v]:
            if not visited[i]:
                num[i] = num[v] + 1
                queue.append(i)
                visited[i] = True
    return sum(num)

for i in range(1, N+1):  
    visited = [False] * (N+1)
    answer.append( bfs(graph, i, visited) )
print(answer.index( min(answer) ) +1 )