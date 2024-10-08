T = int(input())

D = [ (1,0), (0,1), (-1,0), (0,-1) ]
for _ in range(T):
  O = input()
  points = [(0,0)]
  state = 0

  for o in O:
    if o == 'F':
      y = points[-1][0] + D[state][0]
      x = points[-1][1] + D[state][1]
      points.append( (y,x) )
    if o == 'B':
      y = points[-1][0] - D[state][0]
      x = points[-1][1] - D[state][1]
      points.append( (y,x) )
    if o == 'L':
      state -= 1
      state %= 4
    if o == 'R':
      state += 1
      state %= 4

  min_y = 0
  min_x = 0
  max_y = 0
  max_x = 0

  for point in points:
    min_y = min(min_y, point[0])
    min_x = min(min_x, point[1])
    max_y = max(max_y, point[0])
    max_x = max(max_x, point[1])
  print( (max_x - min_x) * (max_y - min_y) )