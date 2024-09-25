N = int(input())

people = []
rank = []
for _ in range(N):
  a, b = map(int, input().split())
  people.append( (a,b) )

for i in range(N):
  count = 0
  for j in range(N):
    if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
      count += 1
  rank.append(count+1)

print(*rank)