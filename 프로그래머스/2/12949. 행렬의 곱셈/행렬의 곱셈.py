def solution(arr1, arr2):
    
    c = len(arr1)
    r = len(arr1[0])
    c2 = len(arr2)
    r2 = len(arr2[0])
    answer = [[0]*r2 for _ in range(c)]
    
    for i in range(c):
        for j in range(r2):
            for k in range(r):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer