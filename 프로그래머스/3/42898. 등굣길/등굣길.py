def solution(m, n, puddles):
    
    graph = [ [0]*m for _ in range(n)]
    r = 1000000007
    graph[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if not [j+1, i+1] in puddles:
                if 0 <= i-1 < n and 0 <= j < m and not [j+1, i] in puddles:
                    graph[i][j] += graph[i-1][j] % r
                if 0 <= i < n and 0 <= j-1 < m and not [j, i+1] in puddles:
                    graph[i][j] += graph[i][j-1] % r

    return graph[n-1][m-1] % r