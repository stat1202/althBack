import sys
input = sys.stdin.readline

N = int(input())

answer = 0
for _ in range(N):
    s = input().rstrip()
    stack = []
    
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        answer += 1
print(answer)