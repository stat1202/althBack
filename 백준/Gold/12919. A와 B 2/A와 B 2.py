S = input()
T = input()

flag = 0
def getWord(t):
  global flag
  if t == S:
    flag = 1
    return
  if t:
    if t[-1] == 'A':
      getWord(t[:-1])
    if t[0] == 'B':
      getWord(t[1:][::-1])

getWord(T)
print(flag)
