import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
woods = list(map(int, input().rstrip().split()))

max_h = max(woods)
min_h = 1
answers = []

while min_h <= max_h:
    now_h = (max_h + min_h) // 2
    my_wood = 0
    for wood in woods:
        if wood > now_h:
            my_wood += wood - now_h

    if my_wood >= M:
        min_h = now_h + 1
    else:
        max_h = now_h - 1

print(max_h)
