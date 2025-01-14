N, M = map(int, input().split())
A = list( map(int, input().split()) )

A.sort()

for _ in range(M):
  n = A[0] + A[1]
  A[0] = n
  A[1] = n
  A.sort()

print(sum(A))