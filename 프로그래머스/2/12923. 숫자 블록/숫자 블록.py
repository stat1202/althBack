def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        n = 0
        
        for j in range(1, min(i // 2 + 1, 10000000) ):
            if i % j == 0:
                n = j
        answer.append(n)
    
    return answer