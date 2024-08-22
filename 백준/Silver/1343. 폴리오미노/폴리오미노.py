board = input()
ans = ""
count = 0
impossible = False
for i in range(len(board)):
  if board[i] == "X":
    count += 1
    if count == 4:
      ans += "AAAA"
      count = 0
  else:
    if count == 0:
      ans += "."
    elif count == 1:
      impossible = True
      break
    elif count == 2:
      ans += "BB."
      count = 0
    elif count == 3:
      impossible = True
      break
if count == 1:
  impossible = True
elif count == 2:
  ans += "BB"
  count = 0
elif count == 3:
  impossible = True

if not impossible:
  print(ans)
else:
  print(-1)


