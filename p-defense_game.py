import heapq

def solution(n, k, enemy):
    l = len(enemy)
    if k >= l:
        return l
    hq = []
    
    for i in range(l):
        heapq.heappush(hq, enemy[i])
        if len(hq) > k:
            min_num = heapq.heappop(hq)
            if min_num > n:
                return i
            n -= min_num
    return l
