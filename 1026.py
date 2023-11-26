import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
answer = 0

A.sort()
B.sort(reverse = True)

for i in range(N):
    answer += A[i] * B[i]
print(answer)