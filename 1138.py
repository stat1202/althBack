import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
nums = [ i for i in range(1, N+1)]
data = list(map(int, input().rstrip().split()))
answer = [0]*N
for i in range(N):
    count = 0
    for j in range(N):
        if count == data[i] and answer[j] == 0:
            answer[j] = i+1
            break
        elif answer[j] == 0:
            count += 1
print(*answer)