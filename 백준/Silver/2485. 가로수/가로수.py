import math
N = int(input())
A = []
distances = []
for _ in range(N):
  A.append(int(input()))

for i in range(1,N):
  distances.append( A[i] - A[i-1] )

gcd = distances[0]
for i in range(1, len(distances)):
  gcd = math.gcd(gcd, distances[i])

answer = 0
for d in distances:
  answer += d // gcd - 1

print(answer)