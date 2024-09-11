# 2313
import heapq
import sys
from sys import maxsize
input = sys.stdin.readline

# print(maxsize)

V, E = map(int, input().split())
start = int(input())
graph = [ [] for i in range(V+1)]
distances = [maxsize] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append( (v,w) )
# print(graph)

def dijkstra(graph, start):
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0,start))

    while queue:
        cur_dist, cur_dest = heapq.heappop(queue)

        if distances[cur_dest] < cur_dist:
            continue
        
        for new_dest, new_dist in graph[cur_dest]:
            distance = cur_dist + new_dist

            if distance < distances[new_dest]:
                distances[new_dest] = distance
                heapq.heappush(queue, [distance, new_dest])
    return distances

answers = dijkstra(graph,start)

for i in range(1, len(answers)):
    if answers[i] == maxsize:
        print("INF")
    else:
        print(answers[i])
    
    

