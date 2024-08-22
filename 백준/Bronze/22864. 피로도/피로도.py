A, B, C, M = map(int, input().split())

time = 0
work = 0
fatigue = 0

while time < 24:
  if fatigue + A <= M:
    fatigue += A
    work += B
  else:
    if fatigue - C < 0:
      fatigue = 0
    else:
      fatigue -= C
  time += 1
print(work)