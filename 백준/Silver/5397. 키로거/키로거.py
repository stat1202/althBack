import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  L = input().rstrip()
  left = []
  right = []

  for l in L:
    if l == '<':
      if left:
        right.append(left.pop())
    elif l == '>':
      if right:
        left.append(right.pop())
    elif l == '-':
      if left:
        left.pop()
    else:
      left.append(l)
  right.reverse()
  
  print(''.join(left) + ''.join(right) )

    