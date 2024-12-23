A, K = map(int, input().split())

count = 0
while K > A:
  if K % 2 == 0 and K / 2 >= A:
    K //= 2
  else:
    K -= 1
  count += 1

print(count)