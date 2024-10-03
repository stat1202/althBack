def solution(targets):
    targets.sort()
    end = 0
    answer = 0
    
    for target in targets:
        t_s, t_e = target
        if t_s >= end:
            end = t_e
            answer += 1
        else:
            end = min(end, t_e)
    
    
    return answer