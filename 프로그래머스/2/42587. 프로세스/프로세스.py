from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([ (priorities[i], i) for i in range(len(priorities))])
    m = max(priorities)
    m_idx = priorities.index(m)
    while q:
        a = q.popleft()
        
        if a[0] == m:
            answer += 1
            priorities[m_idx] = 0
            m = max(priorities)
            m_idx = priorities.index(m)
            if a[1] == location:
                break
        else:
            q.append(a)
        
    return answer
    