import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    queue = deque([(start, 0)])
    visited = [False] * (n+1)
    visited[start] = True
    
    while queue:
        v, d = queue.popleft()
        
        if v == end:
            return d
        
        for i, c in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append( (i, d+c) )
n, m = map(int, input().split())
graph = [ [] for _ in range(n+1)]

for _ in range(n-1):
    n1, n2, c = map(int,input().split())
    graph[n1].append( (n2,c))
    graph[n2].append( (n1,c))
    
for _ in range(m):
    start, end = map(int, input().split())
    answer = bfs(start, end)
    print(answer)
    