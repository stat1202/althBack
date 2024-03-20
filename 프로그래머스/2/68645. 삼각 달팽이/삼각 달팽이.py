def solution(n):
    arr = [ [0]* i for i in range(1,n+1) ]
    num = 1
    c = 0
    while n >= 1:
        i = 0 + c * 2
        j = 0 + c * 1

        for _ in range(n):
            arr[i][j] = num
            num += 1
            i += 1
        for _ in range(n-1):
            j += 1
            arr[i-1][j] = num
            num += 1
        i-=1
        for _ in range(n):
            if arr[i-1][j-1] == 0:
                arr[i-1][j-1] = num
                i -= 1
                j -= 1
                num += 1
        c += 1
        n -= 3
        
    return sum(arr,[])