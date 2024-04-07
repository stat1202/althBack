from collections import Counter
from itertools import combinations

def solution(k, tangerine):
    answer = 0
    count = 0
    counter = Counter(tangerine)
    common = counter.most_common()
    for c in common:
        if count < k:
            count += c[1]
            answer += 1
        else:
            break
    
    
    
    
    return answer