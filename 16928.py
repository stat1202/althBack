import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

counts = [0]*101
visited = [False]* 101
ladders = {}
snakes = {}
for _ in range(N):
    s, e = map(int, input().rstrip().split())
    ladders[s] = e

for _ in range(M):
    s, e = map(int, input().rstrip().split())
    snakes[s] = e


def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        
        if v == 100:
            print(counts[v])
            break
        
        for i in range(1,7):
            new_v = v+i
            
            if new_v <= 100 and not visited[new_v]:
                
                if new_v in ladders:
                    new_v = ladders[new_v]
                elif new_v in snakes:
                    new_v = snakes[new_v]
                    
                if not visited[new_v]:
                    visited[new_v] = True
                    counts[new_v] = counts[v] + 1
                    queue.append(new_v)
            
bfs(1)