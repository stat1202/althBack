import sys
input = sys.stdin.readline
T = int(input().rstrip())

def calendar(M,N, x, y):
    k = x
    while k <= M * N:
        if(k-x) % M == 0 and (k-y)% N == 0:
            return k
        k += M
    return -1

for _ in range(T):
    M,N,x,y = map(int, input().rstrip().split())
    
    print(calendar(M,N,x,y))
   