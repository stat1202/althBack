from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons):
        fatigue = k
        count = 0
        for v in p:
            if fatigue >= v[0]:
                count += 1
                fatigue -= v[1]
        answer = max(count, answer)
    return answer
