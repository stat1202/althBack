def solution(r1, r2):
    answer = 0
    
    y = r1
    count1 = 0
    for x in range(1, r1):
        while x*x + y*y >= r1 * r1:
            y -= 1
        count1 += y
    count1 = 4 * count1 + (r1 -1) * 4 + 1
    
    y = r2
    count2 = 0
    for x in range(1, r2):
        while x*x + y*y > r2 * r2:
            y -= 1
        count2 += y
    count2 = 4 * count2 + r2 * 4 + 1
    
    answer = count2 - count1
    return answer