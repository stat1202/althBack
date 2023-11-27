N = int(input())

maps = []
answer = [[] for _ in range(N)]
direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(N):
    maps.append(list(input()))

for i in range(N):
    for j in range(N):
        if maps[i][j] != ".":
            answer[i].append("*")
        else:
            c = 0
            for d in direction:
                if (0<= i+d[0] < N and 0<= j+d[1] < N )and maps[i + d[0]][j + d[1]] != ".":
                    c += int(maps[i + d[0]][j + d[1]])
            if c > 9:
                c = "M"
            answer[i].append(str(c))

for a in answer:
    print(*a, sep='')