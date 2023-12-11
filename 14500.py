import sys
input = sys.stdin.readline

def dfs(r, c, idx, total):
    global answer
    
    if answer >= total + max_val * (3 - idx):
        return
    if idx == 3:
        answer = max(answer, total)
        return
    else:
        for i in range(4):
            new_r = r + direction[i][0]
            new_c = c + direction[i][1]
            
            if 0 <= new_r < N and 0 <= new_c < M and visited[new_r][new_c] == 0:
                if idx == 1:
                    visited[new_r][new_c] = 1
                    dfs(r, c, idx + 1, total + maps[new_r][new_c])
                    visited[new_r][new_c] = 0
                visited[new_r][new_c] = 1
                dfs(new_r, new_c, idx + 1, total + maps[new_r][new_c])
                visited[new_r][new_c] = 0


N, M = map(int, input().rstrip().split())

maps = []
for _ in range(N):
    maps.append( list( map(int, input().rstrip().split()) ) )

visited = [ [0]*M for _ in range(N)]

direction = [(1,0), (-1,0), (0,1), (0,-1)]
answer = 0
max_val = max(map(max, maps))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, maps[i][j])
        visited[i][j] = 0
print(answer)