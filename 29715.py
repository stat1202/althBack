import sys
input = sys.stdin.readline

def per(num):
    p = 1
    for i in range(1,num+1):
        p *= i
    return p

def com(n, num):
    c = 1
    for i in range(num):
        c *= n
        n -= 1
    return c

N, M = map(int, input().rstrip().split())
X, Y = map(int, input().rstrip().split())
answer = 0
pass_num = 0

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    if a != 0 :
        pass_num += 1
    else:
        N -= 1

max_try = 0
wait_time = 0
if N-pass_num != 0:
    max_try = per(pass_num)* com(9, N-pass_num)
else:
    max_try = per(pass_num)

wait_time = (max_try // 3 - 1) *Y

answer += 3*max_try + wait_time
print(answer)