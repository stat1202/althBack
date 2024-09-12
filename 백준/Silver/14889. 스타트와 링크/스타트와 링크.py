from itertools import combinations
N = int(input())
stat = [ list(map(int, input().split())) for _ in range(N) ]

min_diff = 1e9

for comb in combinations(list(range(N)), N // 2):
  team1 = comb
  team2 = []
  for i in range(N):
    if i not in team1:
      team2.append(i)
  
  score1 = 0
  score2 = 0

  for i in team1:
    for j in team1:
      score1 += stat[i][j]
  
  for i in team2:
    for j in team2:
      score2 += stat[i][j]

  diff = abs(score1 - score2)
  min_diff = min(min_diff, diff)
print(min_diff)