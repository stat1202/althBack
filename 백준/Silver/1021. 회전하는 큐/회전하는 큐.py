import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

nums = list(map(int, input().rstrip().split()))

dq = deque([i for i in range(1,N+1)])

count = 0

for n in nums:
    while True:
        if dq[0] == n:
            dq.popleft()
            break
        else:
            if dq.index(n) < len(dq)/2:
                while dq[0] != n:
                    dq.rotate(-1)
                    count += 1
            else:
                while dq[0] != n:
                    dq.rotate(1)
                    count += 1
print(count)