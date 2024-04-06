def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total//2):
        if total % i == 0:
            h = i
            w = total // i
            if w * 2 + (h-2)*2 == brown:
                return [w,h]