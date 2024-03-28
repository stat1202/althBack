def solution(name, yearning, photo):
    answer = []
    for pho in photo:
        score = 0
        for i in range(len(pho)):
            if pho[i] in name : 
                idx = name.index(pho[i])
                score += yearning[idx]
        answer.append(score)
    return answer