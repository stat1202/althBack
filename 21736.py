import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []
start = (0,0)
for _ in range(N):
    graph.append( list(input().rstrip()) )
for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            start = (i,j)
    
def bfs(graph, start):
    queue = deque( [start] )
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    while queue:
        v = queue.pop()
        # print("v", v)
        for i in range(4):
            nx = dx[i] + v[1]
            ny = dy[i] + v[0]
            if 0 <= ny < N and 0 <= nx < M and ( graph[ny][nx] == "O" or graph[ny][nx] == "P" ):
                queue.append( (ny,nx) )
                if graph[ny][nx] == "P" :
                     count += 1
                graph[ny][nx] = "X"

    return count
answer = bfs(graph, start)
print(answer if answer != 0 else "TT")