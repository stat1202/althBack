def comp(x,y,l,arr):
    init = arr[y][x]
    
    for i in range(y,y+l):
        for j in range(x,x+l):
            if init != arr[i][j]:
                l //= 2
                comp(x,y,l,arr)
                comp(x,y+l,l,arr)
                comp(x+l,y,l,arr)
                comp(x+l,y+l,l,arr)
                return
    answer[arr[y][x]] += 1

def solution(arr):
    global answer
    
    answer = [0,0]
    l = len(arr)
    comp(0,0,l,arr)
    
    return answer