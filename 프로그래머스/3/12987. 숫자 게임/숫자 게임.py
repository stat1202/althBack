def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    i = 0
    j = 0
    while i < len(A):
        if A[i] < B[j]:
            i += 1
            j += 1
            answer += 1
        else:
            j += 1
        
        if j == len(B):
            break
            
    
    return answer