from itertools import permutations

N = int(input())
user_input = []

for _ in range(N):
  user_input.append(list(map(int,  input().split(' ') )))

pers = list(permutations([1,2,3,4,5,6,7,8,9], 3))

# print(user_input)
count = 0

for per in pers:
  flag = 0
  for i in range(N):
    s,b = 0, 0
    n = list(map(int, str(user_input[i][0])))
    
    for j in range(3):
      if per[j] == n[j]:
        s+=1
      else:
        if per[j] in n:
          b+=1
    
    if s != user_input[i][1] or b != user_input[i][2]:
      flag = 0
      break
    else:
      flag = 1
  if flag == 1:
    count += 1

print(count)


