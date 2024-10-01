def solution(n):
    
    start = 0
    num = 0
    answer = [ [0]*n for _ in range(n) ]
    
    while n > 0:
        i = start
        j = start
        # left to right 방향
        for _ in range(n):
            num += 1
            answer[i][j] = num
            j += 1
        j -= 1
        i += 1

        for _ in range(n-1):
            num += 1
            answer [i][j] = num
            i += 1

        i -= 1
        j -= 1

        for _ in range(n-1):
            num += 1
            answer[i][j] = num
            j -= 1

        i -= 1
        j += 1

        for _ in range(n-2):
            num += 1
            answer[i][j] = num
            i -= 1

        n -= 2
        start += 1
            
        
    return answer