import sys
input = sys.stdin.readline

while True:
  try: 
    S, T = input().split()

    pos = 0
    flag = True
    for i in range(len(S)):
      while pos < len(T) and T[pos] != S[i]:
        pos += 1

      if pos < len(T):
        pos += 1
      else:
        flag = False
        break
    if flag:
      print("Yes")
    else:
      print("No")
  except:
    break