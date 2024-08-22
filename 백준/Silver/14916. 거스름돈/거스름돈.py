n = int(input())

cost5 = n // 5
cost2 = 0
flag = True
while True:
  rest = n - cost5 * 5

  if rest % 2 == 0:
    cost2 = rest // 2
    break
  else:
    if cost5 > 0:
      cost5 -= 1
    else:
      flag = False
      break
if flag:
  print(cost5 + cost2)
else:
  print(-1)
