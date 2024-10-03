from itertools import combinations
def solution(board):
    O = []
    X = []
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            v = board[i][j]
            if v == 'O':
                O.append( (i,j) )
            if v == 'X':
                X.append( (i,j) )
    O.sort()
    X.sort()
    lo = len(O)
    lx = len(X)
    
    sheet = [ [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], 
                [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)], 
             [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)] ]
    
    # O의 개수는 x와 같거나 하나만 많아야함
    if lo == lx or lo == lx + 1:
        co = 0
        cx = 0
        
        for comb in combinations(O, 3):
            if list(comb) in sheet:
                
                co += 1
        for comb in combinations(X, 3):
            if list(comb) in sheet:
                cx += 1
        if co == 0 and cx == 0:
            answer = 1
        if co == 1 and cx == 0 and lo == lx + 1:
            answer = 1    
        if co == 2 and cx == 0 and lo == lx + 1:
            answer = 1
        if co == 0 and cx == 1 and lo == lx:
            answer = 1
    return answer