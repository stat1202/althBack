from itertools import combinations

N = int(input())
A = list(map(int,input().split()))

check = [False] * 2000001

for i in range(1, N + 1):
  for comb in combinations(A, i):
    check[sum(comb)] = True

for i in range(1, 2000001):
  if check[i] == False:
    print(i)
    break
