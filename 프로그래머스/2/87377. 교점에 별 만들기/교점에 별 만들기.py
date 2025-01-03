def solution(line):
    points_y = []
    points_x = []
    answer = []
    l = len(line)
    for i in range(l):
        for j in range(i + 1, l):
            A, B, E = line[i]
            C, D, F = line[j]
            bottom = A*D - B*C
            
            if bottom == 0:
                continue
            x = (B*F - E*D) / bottom
            y = (E*C - A*F) / bottom
            
            if x == int(x) and y == int(y):                
                points_x.append(int(x))
                points_y.append(int(y))
    h = max(points_y) - min(points_y)
    w = max(points_x) - min(points_x) 
    base_y = - min(points_y)
    base_x = - min(points_x)
    
    rect = [["."] * (w+1) for _ in range(h+1)]
    for i in range(len(points_x)):
        
        x = points_x[i]
        y = points_y[i]
        rect[y + base_y][x + base_x] = "*"
    
    rect.reverse()
    
    for r in rect:
        answer.append("".join(r))
    return answer