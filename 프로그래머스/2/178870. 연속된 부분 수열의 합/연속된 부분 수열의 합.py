def solution(sequence, k):
    total = 0
    start = 0
    end = -1
    answer = []
    
    while True:
        if total < k:
            end += 1
            if end >= len(sequence):
                break
            total += sequence[end]
        else:
            total -= sequence[start]
            if start >= len(sequence):
                break
            start += 1
        if total == k:
            answer.append( (end-start, (start, end)) )
        
    answer.sort()
    
    return answer[0][1]