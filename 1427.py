import sys
input = sys.stdin.readline

N = list(input().rstrip())
N.sort(reverse = True)
print(*N, sep="")