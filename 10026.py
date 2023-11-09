from collections import deque
import copy
import sys
input = sys.stdin.readline

def bfs(graph, start, N, color, t):
    queue = deque([start])
    d = [ (1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        y,x = queue.pop()
        for i in range(4):
            new_y = y + d[i][0]
            new_x = x + d[i][1]
            if t == "n":
                if 0<= new_y < N and 0 <= new_x < N and graph[new_y][new_x] == color:
                    queue.append( (new_y, new_x) )
                    graph[new_y][new_x] = "V"
            else:
                if 0<= new_y < N and 0 <= new_x < N:
                    if color == "R" or color == "G":
                        if graph[new_y][new_x] == "R" or graph[new_y][new_x] == "G":
                            queue.append((new_y, new_x))
                            graph[new_y][new_x] = "V"
                    else:
                        if graph[new_y][new_x] == color:
                            queue.append( (new_y, new_x) )
                            graph[new_y][new_x] = "V"


N = int(input())
graph = [ list( input().rstrip() ) for _ in range(N) ]

# print(graph)

graph2 = copy.deepcopy(graph)
answer = [0,0]
for i in range(N):
    for j in range(N):
        if graph[i][j] != "V":
            bfs(graph, (i,j), N, graph[i][j], "n" )
            answer[0] += 1
        if graph2[i][j] != "V":
            bfs(graph2, (i,j), N, graph2[i][j], "w" )
            answer[1] += 1
print(*answer)