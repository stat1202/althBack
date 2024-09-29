N = int(input())
A = list(map(int, input().split()))

stack = []
answer = [-1] * N

for i in range(N-1, -1, -1):
  while stack and stack[-1] <= A[i]:
    stack.pop()

  stack.append(A[i])

  if len(stack) > 1:
    answer[i] = stack[-2]

print(*answer)