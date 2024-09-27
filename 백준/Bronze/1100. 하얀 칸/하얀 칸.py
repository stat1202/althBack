A = []

for _ in range(8):
  A.append(input())

answer = 0
for i in range(8):
  for j in range(8):
    if i % 2 == 0:
      if j % 2 == 0:
        if A[i][j] == 'F':
          answer += 1
    else:
      if j % 2 == 1:
        if A[i][j] == 'F':
            answer += 1

print(answer)