# n 전체 사람 수
# 둘쨰 줄 서로 다른 두 사람의 번호

from collections import deque

n = int(input())
start,end = map(int, input().split())
m = int(input())

graph = [ [] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s]. append(e)
    graph[e].append(s)

# print(graph)

def bfs(graph, node, visited):
    nums = [0] * (n+1)
    queue = deque([node])
    visited[node] = True

    while queue:
        v = queue.popleft()
        # print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                nums[i] += nums[v] + 1
                visited[i] = True
    return nums[end]
answer = bfs( graph, start, visited)
print( -1 if answer == 0 else answer)