import heapq

def solution(n, works):
    answer = 0
    max_q = [-w for w in works]
    heapq.heapify(max_q)
    
    for i in range(n):
        a = heapq.heappop(max_q)
        if a < 0:
            a += 1
            heapq.heappush(max_q, a)
        else:
            heapq.heappush(max_q, a)
    
    for i in max_q:
        answer += i**2
    return answer

            
    