import sys
from itertools import permutations
input = sys.stdin.readline

N, K = map(int, input().rstrip().split(' '))
kits = list(map(int, input().rstrip().split(' ')))

after_exercise = [ kit-K for kit in kits]


cnt = 0

for p in list(permutations(after_exercise)):
  weight = 500
  # flag = True
  for i in p:
    weight += i
    if weight < 500:
      # flag = False
      break
  else:
    cnt += 1
print(cnt)