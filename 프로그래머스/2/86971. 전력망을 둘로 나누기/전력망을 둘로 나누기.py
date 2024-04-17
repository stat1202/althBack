from collections import deque

def bfs(graph, s, visited):
    queue = deque([s] )    
    visited[s] = True
    count = 0
    while queue:
        v = queue.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return count

def solution(n, wires):
    answer = n-2
    
    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for _ in range(n+1)]
        visited = [False]* (n+1)
        tmps.pop(i)
        for w in tmps:
            a,b = w
            graph[a].append(b)
            graph[b].append(a)
        for idx, g in enumerate(graph):
            if g != []:
                start = idx
                break
        cnts = bfs(graph, start, visited)
        other_cnts = n - cnts
        answer = min( abs(cnts - other_cnts), answer )
            
    return answer