T = int(input ())
answer = [ [ i for i in range(0, 15) ] ] + [ [0]*15 for _ in range(14)]

for i in range(1, 15):
    for j in range(1, 15):
        # print(i,j)

        for a in range(i-1, i):
            for b in range(0, j+1):
                answer[i][j] += answer[a][b]
# print(answer)
for _ in range(T):
    k = int(input())
    n = int(input())
    print(answer[k][n])