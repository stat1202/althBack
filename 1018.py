import sys
input = sys.stdin.readline

n, m = map(int, input().split() )

grid = []
answer = []

for _ in range(n):
    grid.append( input().rstrip() )

for y in range(n-7):
    for x in range(m-7):
        w = 0
        b = 0
        for i in range(y, y+8):
            for j in range(x, x+8):
                if (i+j) % 2 == 0:
                    if grid[i][j] != "W":
                        w += 1
                    else:
                        b += 1
                else:
                    if grid[i][j] != "W":
                        b += 1
                    else:
                        w += 1
        answer.append(w)
        answer.append(b)
print(min(answer))