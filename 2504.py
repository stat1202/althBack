brackets = input()

stack = []
answer = 0
tmp = 1

for i in range(len(brackets)):
  bracket = brackets[i]
  if bracket == '(':
    stack.append(bracket)
    tmp *=2
  elif bracket == '[':
    stack.append(bracket)
    tmp *=3
  elif bracket == ')':
    if len(stack) == 0 or stack[-1] =='[':
      answer=0
      break
    if brackets[i-1] =='(' :
      answer += tmp
    tmp //= 2
    stack.pop()
  elif bracket == ']':
    if len(stack) == 0 or stack[-1] =='(':
      answer = 0
      break
    if brackets[i-1] =='[' :
      answer += tmp
    tmp //= 3
    stack.pop()

if len(stack) == 0 :
  print(answer)
else:
  print(0)