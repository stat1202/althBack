def solution(rows, columns, queries):
    answer = []
    matrix = [ [0] * columns for _ in range(rows) ]
    
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = cnt
            cnt += 1
    
    for q in queries:
        x1, y1, x2, y2 = q
        n = rotate(x1, y1, x2, y2, matrix)
        answer.append(n)
    return answer

def rotate(x1, y1, x2, y2, matrix):
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    num = 1e9
    save = 0
    
    for y in range(y2, y1, -1):
        if y == y2:
            save = matrix[x1][y]
        matrix[x1][y] = matrix[x1][y-1]
        num = min(matrix[x1][y], num)
        
    save2 = 0
    for x in range(x2, x1, -1):
        if x == x2:
            save2 = matrix[x][y2]
        matrix[x][y2] = matrix[x-1][y2]
        num = min(matrix[x][y2], num)
    matrix[x1+1][y2] = save
    
    save3 = 0
    for y in range(y1, y2):
        if y == y1:
            save3 = matrix[x2][y]
        matrix[x2][y] = matrix[x2][y+1]
        num = min(matrix[x2][y], num)
    matrix[x2][y2-1] = save2
    
    for x in range(x1, x2):
        matrix[x][y1] = matrix[x+1][y1]
        num = min(matrix[x][y1], num)
    matrix[x2-1][y1] = save3
    
    num = min( num, save, save2, save3)
    
    return num
    