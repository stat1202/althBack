import heapq

def solution(operations):
    max_q = []
    min_q = []
    
    for o in operations:
        c, n = o.split()
        if c == "I":
            heapq.heappush(max_q, -int(n))
            heapq.heappush(min_q, int(n))
        elif c == "D":
            if n == "1" and max_q:
                num = heapq.heappop(max_q)
                min_q.remove(-num)
            elif n == "-1" and min_q:
                num = heapq.heappop(min_q)
                max_q.remove(-num)        
    if min_q and max_q:
        return [-heapq.heappop(max_q), heapq.heappop(min_q)]
    else:
        return [0,0]
        