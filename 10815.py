N = int(input())
sangguen = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

dic = {}

for c in cards:
    dic[c] = 0

for s in sangguen:
    if s in dic:
        dic[s] = 1

for d in dic:
    print(dic[d], end=' ')