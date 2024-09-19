import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    answer = 1

    closet = {}
    for _ in range(N):
        c, kind = input().rstrip().split()
        if not kind in closet.keys():
            closet[kind] = 1
        else:
            closet[kind] += 1
    for c in closet:
        answer *= ( closet[c] + 1)
    print(answer -1)