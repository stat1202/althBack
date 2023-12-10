import sys
input = sys.stdin.readline
A, B, C = map(int, input().rstrip().split())

def solution(a,b,c):
    if b==1:
        return a%c
    tmp = solution(a, b//2, c)
    
    if b%2 == 0:
        return tmp*tmp %c
    else:
        return tmp*tmp*a%c
    
print(solution(A,B,C))