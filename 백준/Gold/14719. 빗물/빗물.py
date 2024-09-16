H, W = map(int, input().split())

blocks = (list(map(int, input().split())))
answer = 0

for i in range(1, W-1):
  left = max( blocks[:i] )
  right = max( blocks[i+1:] )
  rain = min(left, right) - blocks[i]

  if rain > 0:
    answer += rain

print(answer)