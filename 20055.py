from collections import deque
import sys
N, K = map(int, input().rstrip().split())
belts = deque(list(map(int, input().rstrip().split())))
robots = deque([False]* N)
answer = 0

while True:
    belts.rotate(1)
    robots.rotate(1)
    robots[-1] = False
    
    if True in robots:
        for i in range(N-2, -1, -1):
            if robots[i] == 1 and robots[i+1] == 0 and belts[i+1] >= 1:
                robots[i+1] = True
                robots[i] = False
                belts[i+1] -= 1
        robots[-1] = False
    if not robots[0] and belts[0] >= 1:
        robots[0] = True
        belts[0] -= 1
    answer += 1
    if belts.count(0) >= K:
        break
print(answer)        