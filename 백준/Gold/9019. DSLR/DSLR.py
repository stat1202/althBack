from collections import deque
# D n을 두 배로 바꾸고 나누기 10000을 레지스터에 저장
# S n-1을 레지스터에 저장 n이 0이면 9999
# L 1234 -> 2341
# R 1234 -> 4123

def bfs(start, end, visited):
    q = deque([ (start, "") ])
    while q:
        v = q.popleft()
        
        if v[0] == end:
            return v[1]
        
        d = (v[0] * 2) % 10000
        s = v[0]-1 if v[0] > 0 else 9999
        l = v[0] // 1000 + (v[0] % 1000)*10
        r = v[0] // 10 + (v[0] % 10) * 1000
        
        if not visited[d]:
            q.append( (d, v[1] + "D") )
            visited[d] = True
        if not visited[s]:
            q.append( (s, v[1] + "S") )
            visited[s] = True
        if not visited[l]:
            q.append( (l, v[1] + "L") )
            visited[l] = True
        if not visited[r]:
            q.append( (r, v[1] + "R") )
            visited[r] = True
        

T = int(input())
for _ in range(T):
    start, end = map(int, input().split())
    visited = [False]* 10000

    answer = bfs(start, end, visited)
    print(answer)
    
        
        
    
    