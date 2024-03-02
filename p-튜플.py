from collections import Counter
def solution(s):
    answer = []
    a = s.replace("{", "").replace("}","").split(",")
    counter = Counter(a).most_common() 
    for a,_ in counter:
        answer.append(int(a))
        
    return answer
