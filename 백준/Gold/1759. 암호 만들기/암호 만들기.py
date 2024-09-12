from itertools import combinations

L, C = map(int, input().split())

s = input().split()
s.sort()

for c in combinations(s, L):
  count = 0
  if 'a' in c:
    count += 1
  if 'e' in c:
    count += 1
  if 'i' in c:
    count += 1
  if 'o' in c:
    count += 1
  if 'u' in c:
    count += 1
  
  if count > 0 and L - count >= 2:
    print("".join(c))