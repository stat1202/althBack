def solution(plans):
    answer = []
    stack = []
    # plans 시간 변환
    for i in range(len(plans)):
        h,m = map(int, plans[i][1].split(":"))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key = lambda x : x[1])
    
    for i in range(1, len(plans)):
        n, s, p = plans[i-1]
        rest = plans[i][1] - s
        
        stack.append([n, s, p])
        
        while stack and rest:
            if stack[-1][2] <= rest:
                rest -= stack[-1][2]
                plan = stack.pop()
                answer.append(plan[0])
            else:
                stack[-1][2] -= rest
                rest = 0
    answer.append(plans[-1][0])
    
    while stack:
        plan = stack.pop()
        answer.append(plan[0])

    return answer