# 2100
import sys
from sys import maxsize
input = sys.stdin.readline

def bf(start):
    dist = [10000] * (N+1)
    dist[start] = 0

    for i in range(N):
        for s,d,w in graph:
            if dist[s] != maxsize and dist[d] > dist[s] + w:
                dist[d] = dist[s] + w
                
                if i == N-1:
                    return False
    return True


TC = int( input() )
for _ in range(TC):
    # N, M, W
    N,M,W = map(int, input().split())
    graph = []

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph.append( (a,b,c) )
        graph.append( (b,a,c) )
    for _ in range(W):
        a, b, c = map(int, input().split())
        graph.append( (a,b,-c) )

    answer = bf(1)
    if answer:
        print("NO")
    else:
        print("YES")

