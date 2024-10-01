import heapq
import math

def solution(picks, minerals):
    answer = 0
    table = [ [1, 1, 1], [5, 1, 1], [25, 5, 1] ]
    index = {
        "diamond": 0,
        "iron": 1,
        "stone": 2
    }
    
    picks_list = []
    pq = []
    minerals = minerals[ : sum(picks) * 5]
    
    for i in range(0, len(minerals), 5):
        tmp = [0,0,0]
        for mineral in minerals[i:i+5]:
            tmp[index[mineral]] -= 1
        heapq.heappush(pq, tmp)
    
    while pq:
        mineral = heapq.heappop(pq)
        pirodo = 0
        p_idx = 0
        
        for i in range(len(picks)):
            if picks[i] != 0:
                for j in range(len(mineral)):
                    pirodo += -table[i][j] * mineral[j]
                picks[i] -= 1
                break
            
        answer += pirodo
                    
    return answer