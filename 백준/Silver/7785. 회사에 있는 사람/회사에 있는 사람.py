import sys

input = sys.stdin.readline

n = int(input())
log = {}

for _ in range(n):
  data = input().rstrip().split(" ")
  name, state = data
  if state == 'enter':
    log[name] = 1
  else:
    log[name] = 0

result = []

for key in log:
  if log[key] == 1:
    result.append(key)
result.sort(reverse=True)

for r in result:
  print(r)