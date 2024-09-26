from itertools import combinations

A = [int(input()) for _ in range(9)]


answer = []
for comb in combinations(A, 7):
  if sum(comb) == 100:
    answer = list(comb)
    break

for a in answer:
  print(a)