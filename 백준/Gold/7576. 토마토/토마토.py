# 1400
from collections import deque
m,n = map(int, input().split())


location = []
graph = []
ones = []
for i in range(n):
    tmp = list( map(int, input().split()) )
    for j in range(m):
        if tmp[j] == 1:
            ones.append( (i,j))
    graph.append(tmp)
# print(n0)
d = [(-1,0), (1,0), (0,-1), (0,1)]
# m => x n => y
res = 0

# print(ones)
# print(graph)
def bfs (graph, ones):
    queue = deque( ones )
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0<= nx < m and 0<=ny < n :
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append( (ny,nx))
    # return {count: count, answer : answer}
# print(location)
bfs(graph, ones)
# for i in graph:
#     for j in i:
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1 )