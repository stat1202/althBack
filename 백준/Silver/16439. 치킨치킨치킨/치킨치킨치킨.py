from itertools import combinations

N, M = map(int, input().split())

chickens = [list(map(int, input().split())) for _ in range(N)]

max_happy = 0

for comb in combinations( range(M) , 3):
  total_happy = 0
  for chicken in chickens:
    happy = 0
    for c in comb:
      happy = max(happy, chicken[c])
    total_happy += happy
  
  max_happy = max(max_happy, total_happy)

print(max_happy)

