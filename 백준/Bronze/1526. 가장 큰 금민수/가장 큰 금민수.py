from itertools import product
N = int(input())

A = []
for i in range(1, 7):
  for prod in product([4,7], repeat=i):
    keum = 0
    for n in prod:
      keum *= 10
      keum += n
    A.append(keum)

for a in A[::-1]:
  if a <= N:
    print(a)
    break