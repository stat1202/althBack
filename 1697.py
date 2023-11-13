from collections import deque
import sys
input = sys.stdin.readline

MAX_VALUE = 100000
N, K = map(int, input().rstrip().split())

counts = [0] * (MAX_VALUE + 1)

def bfs(counts, start, end):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        back = v - 1
        front = v + 1
        tel = v * 2
        if 0<= back <= MAX_VALUE and not counts[back]:
            queue.append(back)
            counts[back] = counts[v] + 1
        if 0<= front <= MAX_VALUE and not counts[front]:
            queue.append(front)
            counts[front] = counts[v] + 1
        if 0<= tel <= MAX_VALUE and not counts[tel]:
            queue.append(tel)
            counts[tel] = counts[v] + 1
        if back == end or front == end or tel == end:
            break
if N == K:
    print(0)
else:
    bfs(counts, N, K)
    print(counts[K])
