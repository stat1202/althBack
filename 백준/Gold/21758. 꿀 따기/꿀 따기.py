N = int(input())
honey = list(map(int, input().split()))

psum = [0] * N

for i in range(N):
  if i == 0:
    psum[i] = honey[i]
  else:
    psum[i] = psum[i-1] + honey[i]

answer = psum[N-2] - psum[0] + max(honey[1:-1])

for i in range(1, N-1):
  a = psum[N-1] - psum[0] - honey[i]
  b = psum[N-1] - psum[i]
  answer = max(answer, a + b)

for i in range(1, N-1):
  a = psum[N-2] - honey[i]
  b = psum[i-1]
  answer = max(answer , a + b)

print(answer)
