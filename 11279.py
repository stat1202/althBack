import heapq
import sys

input = sys.stdin.readline

heap = []
n = int(input())

for _ in range(n):
    num = int(input())
    
    if num == 0:
        if heap:
            print( -1 * heapq.heappop(heap) )
        else:
            print(0)
    else:
        heapq.heappush(heap, -1 * num)
    