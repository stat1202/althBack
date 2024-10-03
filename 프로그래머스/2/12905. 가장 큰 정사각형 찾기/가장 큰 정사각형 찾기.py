from collections import deque
def solution(board):
    answer = 0
    
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                if board[i-1][j] != 0 and board[i][j-1] != 0 and board[i-1][j-1] != 0:
                    board[i][j] = min( board[i-1][j], board[i][j-1], board[i-1][j-1] ) + 1
    
    for b in board:
        tmp = max(b)
        answer = max(tmp, answer)
    return answer * answer