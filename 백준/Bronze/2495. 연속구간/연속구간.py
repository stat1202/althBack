for _ in range(3):
  answer = 0
  N = input()
  s = ''

  for n in N:
    if not s:
      s += n
    else:
      if s[-1] == n:
        s += n
      else:
        s = n
    answer = max(len(s), answer)
  
  print(answer)
