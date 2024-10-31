N = int(input())
A = []
for _ in range(N):
  y,x = map(int, input().split())
  A.append((y,x))

max_plus = -1e9
min_plus = 1e9

for y, x in A:
  max_plus = max(max_plus, y+x)
  min_plus = min(min_plus, y+x)

max_minus = -1e9
min_minus = 1e9

for y,x in A:
  max_minus = max(max_minus, y-x)
  min_minus = min(min_minus, y-x)

print(max(max_plus - min_plus, max_minus - min_minus))