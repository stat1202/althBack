import sys
from collections import  deque

input = sys.stdin.readline

def bfs(graph):
    visited = [0]*(N+1)
    q = deque()
    q.append(1)
    visited[1] = 1
    
    while q:
        v = q.popleft()
        
        for i in graph[v]:
            if visited[i] == 0 :
                visited[i] = v
                q.append(i)
    return visited


N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().rstrip().split() )
    graph[a].append(b)
    graph[b].append(a)

answer = bfs(graph)

for a in answer[2:]:
    print(a)

        
