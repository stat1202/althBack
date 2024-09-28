import sys
input = sys.stdin.readline

S = input().rstrip()
trigger = input().rstrip()

stack = []
for s in S:
  if not stack:
    stack.append(s)
  else:
    if "".join(stack[-(len(trigger)):]) == trigger:
      for _ in range(len(trigger)):
        stack.pop()
    stack.append(s)

if "".join(stack[-(len(trigger)):]) == trigger:
  for _ in range(len(trigger)):
    stack.pop()

if stack:
  print("".join(stack))
else:
  print("FRULA")
