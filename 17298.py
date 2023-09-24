n = int(input())
sequence = list(map(int, input().split() ))

answer = [-1]*n
stack = [0]

for i in range(1,n):
    while stack and sequence[ stack[-1] ] < sequence[i]:
        
        answer[stack.pop()] = sequence[i]
    stack.append(i)

print(*answer)
