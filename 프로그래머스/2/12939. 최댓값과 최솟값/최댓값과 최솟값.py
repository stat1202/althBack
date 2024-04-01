def solution(s):
    sp = list(map(int, s.split(" ")))
    answer = f'{min(sp)} {max(sp)}'
    return answer