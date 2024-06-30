from collections import deque

T = int(input())

for _ in range(T):
  d = input()
  answer = deque([])
  cursor = 0
  for i in d:
    if i == "<":
      if cursor > 0:
        cursor -= 1
    elif i == ">":
      if cursor < len(answer):
        cursor += 1
    elif i == "-":
      if cursor > 0: 
        del answer[cursor - 1]
        cursor -= 1 
    else:
      answer.insert(cursor, i)
      cursor += 1
  print("".join(answer) )