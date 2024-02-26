from collections import deque

def bfs(start, end, maps):
    queue = deque([start])
    distances = [[0]* len(maps[0]) for _ in range(len(maps))]
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    while queue:
        y,x = queue.popleft()
        for d in directions:
            new_y = y + d[0]
            new_x = x + d[1]
            if 0<= new_y < len(maps) and 0<= new_x < len(maps[0]):
                if not maps[new_y][new_x] == "X" and distances[new_y][new_x] == 0:
                    queue.append( (new_y,new_x) )
                    distances[new_y][new_x] = distances[y][x] + 1
    return distances[end[0]][end[1]]

def solution(maps):
    start = (0,0)
    end = (0,0)
    lever = (0,0)
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                start = (i,j)
            elif maps[i][j] == "E":
                end = (i,j)
            elif maps[i][j] == "L":
                lever = (i,j)
    stol = bfs(start, lever, maps)
    ltoe = bfs(lever, end, maps)
    
    return stol + ltoe if stol != 0 and ltoe != 0 else -1
    
