def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        n = 0
        if i != 1:
            n = 1
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    if i // j > 10000000:
                        n = max(n, j)
                    else:
                        n = max([n, i//j, j])
        answer.append(n)
    
    return answer