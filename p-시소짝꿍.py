from collections import Counter
def solution(weights):
    answer = 0
    counts = Counter(weights)
    
    for c in counts:
        n = counts[c]
        if  n > 1:
            answer += n*(n-1)//2
            
    weights_set = set(weights)    
    
    for w in weights_set:
        if w * 2/3  in weights_set:
            answer += counts[w*2/3] * counts[w]
        if w * 2/4  in weights_set:
            answer += counts[w*2/4] * counts[w]
        if w * 3/4  in weights_set:
            answer += counts[w*3/4] * counts[w]
    
    return answer
