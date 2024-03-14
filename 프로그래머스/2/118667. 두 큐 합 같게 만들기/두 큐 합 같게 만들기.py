from collections import deque

def solution(queue1, queue2):
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    c1 = 0
    c2 = 0
    s1 = sum(q1)
    s2 = sum(q2)
    answer = 0
    while c1 < len(queue1) or c2 < len(queue2):
        if s1 > s2:
            tmp = q1.popleft()            
            q2.append( tmp )
            s1 -= tmp
            s2 += tmp
            c1 += 1
            answer += 1
        elif s1 < s2:
            tmp = q2.popleft() 
            q1.append( tmp )
            s2 -= tmp
            s1 += tmp
            
            c2 += 1
            answer += 1
        else:
            break
        
    if c1 == len(queue1) or c2 == len(queue2):
        return -1
    
    return answer