from collections import deque

def solution(order):
    answer = 0
    sub = deque([])
    main_belt = deque([i for i in range(1, 1000001)])
    i = 1
    order = deque(order)
    
    while order:
        if i == order[0]:
            answer += 1
            i += 1
            order.popleft()
        elif i < order[0]:
            sub.appendleft(i)
            i += 1
        else:
            if sub[0] == order[0]:
                answer += 1
                sub.popleft()
                order.popleft()
            else:
                break
    
    return answer