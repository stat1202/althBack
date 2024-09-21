grid = list(input())

box = 0
goal = 0
robot = 0

for i in range(len(grid)):
  if grid[i] == '@':
    robot = i
  if grid[i] == '#':
    box = i
  if grid[i] == '!':
    goal = i

if (robot < box and box < goal) or (robot > box and box > goal):
  print( abs(goal - robot) - 1)
else:
  print(-1)


