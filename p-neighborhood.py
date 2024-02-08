def solution(board, h, w):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    answer = 0
    l = len(board)
    for d in directions:
        y = h + d[0]
        x = w + d[1]
        if 0 <= y < l and 0 <= x < l:
            if board[y][x] == board[h][w]:
                answer += 1
    return answer
