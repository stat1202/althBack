import sys
input = sys.stdin.readline

N = int(input())
A = {}
B = {}
classes = set()
answer = N

for n in map(int, input().split()):
  if not n in A:
    A[n] = 0
  A[n] += 1
  classes.add(n)


for n in map(int, input().split()):
  if not n in B:
    B[n] = 0
  B[n] += 1
  classes.add(n)


if len(A) > len(B):
  A, B = B, A

for cl in classes:
  if cl in A and cl in B:
    answer -= min( A[cl], B[cl] )

print(answer)
