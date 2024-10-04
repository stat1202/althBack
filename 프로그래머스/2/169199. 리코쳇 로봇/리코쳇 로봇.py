from collections import deque
dx=[-1,1,0,0]
dy=[0,0,1,-1]
 
def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    q = deque()
    dist = [[1e9 for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i,j,0))
                dist[i][j] = 0
                
    while q:
        y, x, c = q.popleft()
        
        if board[y][x] == 'G':
            return c
        
        for i in range(4):
            n_y = y
            n_x = x
            
            while 0 <= n_y+dy[i] < N and 0 <= n_x+dx[i] < M and board[n_y+dy[i]][n_x+dx[i]] != 'D':
                n_y += dy[i]
                n_x += dx[i]
            
            if dist[n_y][n_x] > c+1:
                dist[n_y][n_x] = c+1
                q.append((n_y,n_x,c+1))
    
    return -1
