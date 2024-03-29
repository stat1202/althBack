def solution(park, routes):
    result = []
    obstacles = []
    graph = [ [0]*len(park[0]) for _ in range( len(park) ) ]
    
    for i in range( len(park) ):
        for j in range( len(park[i])):
            # print( park[i][j])
            if park[i][j] == "S":
                result.append( (i,j) )
            elif park[i][j] == "X":
                graph[i][j] = -1
    # print(graph)
    # print(result)
    for route in routes:
        # print(route)
        d, n = route.split(" ")
        n = int(n)
        y,x = result[-1]
        if d == "E":
            if result[-1][1] + n < len(park[0]):
                for i in range(1, n+1):
                    x = result[-1][1] + i
                    if graph[y][x] == -1:
                        break
        elif d == "W":
            if result[-1][1] - n >= 0:
                for i in range(1, n+1):
                    x = result[-1][1] - i
                    if graph[y][x] == -1:
                        break
        elif d == "S":
            if result[-1][0] + n < len(park):
                for i in range(1,n+1):
                    y = result[-1][0] + i
                    if graph[y][x] == -1:
                        break
        elif d == "N":
            if result[-1][0] - n >= 0:
                for i in range(1,n+1):
                    y = result[-1][0] - i
                    if graph[y][x] == -1:
                        break
        if graph[y][x] != -1:
            result.append( (y,x) )
    # print(result)
    return result[-1]
        