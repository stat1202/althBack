from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.pop()
        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

N, M = map(int, input().rstrip().split() )

visited = [False] * (N+1)
graph = [ [] for _ in range(N+1)]
answer = 0
for _ in range(M):
    s, e = map(int, input().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited)
        answer += 1
print(answer)
