def solution(N, road, K):
    answer = 0
    A = [ [1e9] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i][j] = 0
                
    for a,b,c in road:
        A[a-1][b-1] = min(A[a-1][b-1],c)
        A[b-1][a-1] = min(A[b-1][a-1],c)
    
    for k in range(N):
        for s in range(N):
            for e in range(N):
                A[s][e] = min(A[s][e], A[s][k] + A[k][e])
    for a in A[0]:
        if a <= K:
            answer += 1
    
    return answer