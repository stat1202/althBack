import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list( map(int, input().split()) )

cnt = [0] * 100001

start = 0
end = 0
cnt[A[start]] += 1
max_l = 0

flag = True

while True:
  if flag:
    max_l = max(max_l, end - start + 1)

    if end == N-1:
      break
    end += 1
    cnt[A[end]] += 1
    if cnt[A[end]] == K + 1:
      flag = False
  else:
    start += 1
    cnt[A[start-1]] -= 1
    if cnt[A[start-1]] == K:
      flag = True

print(max_l)