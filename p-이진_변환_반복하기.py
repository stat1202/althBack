from collections import Counter
def solution(s):
    answer = [0,0]
    
    while s != "1":
        counter = Counter(s)    
        answer[0] += 1
        answer[1] += counter["0"]
        s = bin(counter["1"])[2:]
        
    return answer
