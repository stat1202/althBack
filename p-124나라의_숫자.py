def solution(n):
    answer = ''
    
    while n:
        r = n % 3
        if r == 0:
            answer = "4" + answer
            n -= 1
        elif r == 1:
            answer = "1" + answer
        elif r == 2:
            answer = "2" + answer
        n //= 3
        
    return answer
