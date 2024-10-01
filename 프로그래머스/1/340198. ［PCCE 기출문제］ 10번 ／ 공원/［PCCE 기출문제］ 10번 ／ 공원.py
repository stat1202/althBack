def solution(mats, park):
    answer = -1
    mats.sort()
    park_y = len(park)
    park_x = len(park[0])
    
    for i in range(park_y):
        for j in range(park_x):
            for mat in mats:
                cnt = 0
                if i + mat <= park_y and j + mat <= park_x:
                    for y in range(i, i + mat, 1):
                        for x in range(j, j + mat, 1):
                            if park[y][x] == "-1":
                                cnt += 1
                            else:
                                break
                if cnt == mat * mat:
                    answer = max(answer,mat)
                else:
                    break
    return answer