import sys
N, K = map(int, input().rstrip().split())

d = list(map(int, input().rstrip().split()))
l = len(d)//2
belts = [ d[0:l], list(reversed(d[l:])) ]

step = 1
count = 0

print(belts)
def move(step, belts):
    global K
    global count
    l = len(belts) // 2
    while count < K:
        print("while 실행", count, step)
        for i in range(step):
            x = i // l
            y = i % l
            print(y, x)
            if belts[y][x] > 0:
                belts[y][x] -= 1
            if belts[y][x] == 0:
                count += 1      
        step += 1

move(step, belts)
print(step)
print(belts)