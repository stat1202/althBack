N = int(input())
A = list(map(int, input().split()))

score = 0
bonus = 0
for a in A:
  if a == 1:
    bonus += 1
    score += bonus
  else:
    bonus = 0
print(score)