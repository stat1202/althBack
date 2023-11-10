from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def bfs(start):
    queue = deque()
    queue.append(start)
    check = [0 for _ in range(N)]
    
    while queue:
        v = queue.popleft()
        
        for i in range(N):
            if check[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[start][i] = 1
for i in range(0, N):
    bfs(i)
for i in visited:
    print(*i)