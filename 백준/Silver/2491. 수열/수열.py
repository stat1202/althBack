N = int(input())
A = list(map(int, input().split()))

max_asc = 1
max_desc = 1
asc = 1
desc = 1

for i in range(1,N):
  if A[i-1] <= A[i]:
    asc += 1
  else:
    asc = 1

  if A[i-1] >= A[i]:
    desc += 1
  else:
    desc = 1
  max_asc = max(max_asc, asc)
  max_desc = max(max_desc, desc)

print(max(max_asc, max_desc))