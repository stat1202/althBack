N = int(input())
answer = 0

for _ in range(N):
  S = input()

  compress_word = ''

  for i in range(len(S)):
    if compress_word == '':
      compress_word += S[i]
      continue

    if compress_word[-1] != S[i]:
      compress_word += S[i]
  
  checker = []
  flag = True
  for w in compress_word:
    if not checker:
      checker.append(w)
      continue
    
    if w in checker:
      flag = False
      break
    else:
      checker.append(w)
  if flag:
    answer += 1
print(answer)