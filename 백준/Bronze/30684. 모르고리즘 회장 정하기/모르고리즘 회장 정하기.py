N = int(input())

names = []

for _ in range(N):
  name = input()

  if len(name) == 3:
    names.append(name)

names.sort()

print(names[0])