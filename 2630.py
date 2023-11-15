import sys
input = sys.stdin.readline

N = int( input() )

papers = [ list( map(int, input().rstrip().split() ) ) for _ in range(N) ]

answer = [0, 0]

def paperSlice(x,y,N):
    color = papers[x][y]
    
    for r in range(x, x+N):
        for c in range(y, y+N):
            if color != papers[r][c]:
                paperSlice(x,y, N//2)
                paperSlice(x,y+ N//2, N//2)
                paperSlice(x+ N//2 ,y, N//2)
                paperSlice(x+N//2,y+N//2, N//2)
                return 0
    if color == 0:
        answer[0] += 1
    else:
        answer[1] += 1
paperSlice(0,0,N)

for a in answer:
    print(a)
