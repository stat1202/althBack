def find_idx(place):
    participants = []
    partitions = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                participants.append( (i,j))
            elif place[i][j] == "X":
                partitions.append( (i,j))
    return [participants, partitions]

def valid(participants, partitions):
    for i in range(len(participants)):
        for j in range(len(participants)):
            if not i == j:
                y,x = participants[i]
                d_y,d_x = participants[j]
                dist = abs(d_y - y) + abs(d_x - x)
                if dist == 1:
                    return 0
                elif dist == 2:
                    if y == d_y:
                        a = (y, min(x, d_x)+1)
                        if a not in partitions:
                            return 0
                    elif x == d_x:
                        a = (min(y, d_y)+1, x)
                        if a not in partitions:
                            return 0
                    else:
                        a_1 = (y,d_x)
                        a_2 = (d_y,x)

                        if not a_1 in partitions or a_2 not in partitions:
                            return 0

    return 1

def solution(places):
    answer = []
    
    for p in places:
        participants, partitions = find_idx(p)
        result = valid(participants, partitions)
        answer.append(result)
        
    return answer