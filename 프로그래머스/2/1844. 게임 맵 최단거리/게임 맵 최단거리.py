from collections import deque

def bfs(graph, n, m, path):
    d = [ (1,0), (-1,0), (0,1), (0,-1)]
    queue = deque( [(0,0)] )
    graph[0][0] = 0
    path[0][0] = 1
    while queue:
        v = queue.popleft()
        y,x = v
        for i in range(4):
            nx = x + d[i][1]
            ny = y + d[i][0]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                queue.append( (ny,nx) )
                graph[ny][nx] = 0
                path[ny][nx] =  path[y][x] + 1
        

def solution(maps):
    n = len(maps)
    m = len( maps[0] )
    
    path = [ [0]*m for _ in range(n) ]
    # print(path)
    # print(maps)
    bfs(maps, n, m, path)
    if path[n-1][m-1] == 0:
        return -1
    else:
        return path[n-1][m-1]
