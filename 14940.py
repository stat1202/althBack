from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start):
    queue = deque( [start])
    d = [ (1,0), (-1,0), (0,1), (0,-1) ]
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            new_y = y + d[i][0]
            new_x = x + d[i][1]
            if 0<= new_y < n and 0 <= new_x < m and graph[new_y][new_x] == 1:
                queue.append( (new_y, new_x) )
                graph[new_y][new_x] = -1
                distances[new_y][new_x] = distances[y][x] + 1

                
n, m = map(int, input().rstrip().split() )

distances = [ [0] * m for _ in range(n) ]
start = (0,0)
graph = []

for i in range(n):
    data = list( map(int, input().rstrip().split() ) )
    graph.append(data)
    for j in range(len(data)):
        if data[j] == 2:
            start = (i,j)

bfs(graph, start)

for i in range(n):
    for j in range(m):
        if not (i == start[0] and j == start[1])  and graph[i][j] == 1 and distances[i][j] == 0:
            distances[i][j] = -1

for distance in distances:
    print(*distance)
