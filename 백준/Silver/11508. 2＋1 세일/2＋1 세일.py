N = int(input())
A = []
for _ in range(N):
  A.append( int(input()) )

A.sort(reverse=True)
discount = 0
for i in range(0, N, 3):
  if i + 2 < N:
    discount += A[i+2]

print(sum(A) - discount)

