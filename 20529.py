import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    mbtis = input().rstrip().split()
    answer = 20
    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    score = 0

                    if i == j or j == k or i == k:
                        continue
                    for n in range(4):
                        if mbtis[i][n] != mbtis[j][n]:
                            score += 1
                        if mbtis[j][n] != mbtis[k][n]:
                            score += 1
                        if mbtis[i][n] != mbtis[k][n]:
                            score += 1
                    answer = min(answer,score)
        print(answer)
