max_p = 0
p = 0
for _ in range(10):

  a, b = map(int, input().split())
  p = p - a + b
  max_p = max(max_p, p)

print(max_p)