from itertools import combinations
N = int(input())

A = []
for i in range(1, 11):
  for comb in combinations(list(range(10)), i):
    decrease = 0 
    for n in comb[::-1]:
      decrease *= 10
      decrease += n
    
    A.append(decrease)
A.sort()

if N >= len(A):
  print(-1)
else:
  print(A[N])