import math

def solution(n, stations, w):
    answer = 0
    idx = 1
    r = w*2 + 1
    
    for station in stations:
        s = station - w
        d = s - idx
        
        if s > 0 and d > 0:
            answer += math.ceil( d/r )
        idx = station + w + 1
        
    if idx <= n:
        d = (n+1) - idx
        answer += math.ceil(d/r)
    
    return answer