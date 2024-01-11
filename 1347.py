n = int(input())
commands = input()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

x,y,direction = 0, 0, 1
position = [ [x,y] ]

for c in commands:
    if c == "R":
        direction = (direction + 1) % 4
    if c == "L":
        direction = (direction - 1) % 4
    if c == "F":
        x = x + dx[direction]
        y = y + dy[direction]
        position.append([x,y])

n = max(position)[0] - min(position)[0] + 1
m = max(position, key = lambda x : x[1])[1] - min(position, key = lambda x : x[1])[1] + 1

min_x = min(position, key = lambda x:x[0])[0]
min_y = min(position, key = lambda x:x[1])[1]

for p in position:
    p[0] = p[0] + abs(min_x)
    p[1] = p[1] + abs(min_y)
    
graph = [ ["#"]*m for _ in range(n) ]
for p in position:
    if graph[p[0]][p[1]] == "#":
        graph[p[0]][p[1]] = "."

for g in graph:
    print(*g, sep="")
        