from collections import deque

def bfs(graph, i, j):
    queue = deque([(i,j)])
    graph[i][j] = 0
    d = [ (1,0), (-1,0), (0,1), (0,-1)]
    
    while queue:
        y,x = queue.popleft()
        for idx in range(4):
            n_y = y + d[idx][0]
            n_x = x + d[idx][1]
            if 0 <= n_y < len(graph) and 0 <= n_x < len(graph[0]) and graph[n_y][n_x] == 1:
                queue.append( (n_y,n_x) )
                graph[n_y][n_x] = 0
            
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [ [0]*M for _ in range(N)]
    count = 0
    
    for _ in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                count += 1
    print(count)
                