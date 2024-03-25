def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    
    for i in range(len(A)):
        tmp = A[i] * B[i]
        answer += tmp

    return answer