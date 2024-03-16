def solution(routes):
    answer = 0
    routes.sort()
    
    stack = []
    min_r = 30000
    for r in routes:
        
        if not stack:
            stack.append(r)
        else:
            if min_r < r[0]:
                answer += 1
                stack = []
                min_r = 30000
            
            stack.append(r)
        min_r = min(min_r, r[1])
    
    if stack:
        answer += 1
    
    return answer