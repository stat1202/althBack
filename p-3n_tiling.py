def solution(n):
    answer = [0, 3, 11]
    idx = n // 2
    if n % 2 != 0:
        return 0
    if idx < 3: return answer[idx]
    
    for i in range(3, idx+1):
        result = (3*answer[i-1] + sum(answer[1:i-1])*2 + 2) % 1000000007
        answer.append(result)
    
    return answer[idx]
