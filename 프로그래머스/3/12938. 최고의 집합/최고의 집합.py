def solution(n, s):
    answer = [ s//n for _ in range(n)]
    r = s%n
    i = 0
    
    if s//n == 0:
        return [-1]
    
    while r:
        
        if i < len(answer):
            answer[i] += 1
            i+=1
        else:
            i = 0
        r -= 1
    
    return answer[::-1]