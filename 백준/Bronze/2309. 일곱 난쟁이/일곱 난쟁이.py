from itertools import combinations

heights = []

for _ in range(9):
  heights.append( int(input()))


for c in combinations(heights, 7):
  if sum(c) == 100:
    c = list(c)
    c.sort()
    for i in c:
      print(i)
    break

