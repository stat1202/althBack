from collections import deque

def bfs(maps, visited, start):
    q = deque([start])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    count = 0
    visited[start[0]][start[1]] = True
    while q:
        y,x = q.popleft()
        count += int(maps[y][x])
        for d in directions:
            n_y = y + d[0]
            n_x = x + d[1]
            if 0<= n_y < len(maps) and 0<= n_x < len(maps[0]) and not visited[n_y][n_x] and not maps[n_y][n_x] == "X":
                visited[n_y][n_x] = True
                q.append( (n_y,n_x))
    return count
                
    
        
        
def solution(maps):
    answer = []
    visited = [ [False]* len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if not visited[i][j] and not maps[i][j] == "X":
                result = bfs(maps,visited, (i,j))
                answer.append(result)
    
    
    return sorted(answer) if answer else [-1]