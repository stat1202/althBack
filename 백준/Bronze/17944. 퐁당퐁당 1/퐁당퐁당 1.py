N, T = map(int, input().split())

count = 0
asc = True
for i in range(1, T+1):

  if count == 1:
    asc = True
  if count == 2 * N:
    asc = False
  
  if asc:
    count += 1
  else:
    count -= 1

print(count)