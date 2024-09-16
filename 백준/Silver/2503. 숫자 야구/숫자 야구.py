from itertools import permutations

N = int(input())

Q = []

for _ in range(N):
  Q.append( input().split() )

count = 0
for p in permutations(range(1,10), 3):
  flag = True

  for i in range(N):
    strike = 0
    ball = 0
    for j in range(3):
      if int( Q[i][0][j] ) == p[j]:
        strike += 1
        continue

      if int( Q[i][0][j] ) in p:
        ball += 1

    if strike != int( Q[i][1] ) :
      flag = False
      break
    if ball != int( Q[i][2] ):
      flag = False
      break
    

  if flag:
    count += 1

print(count)