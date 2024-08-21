import sys
input = sys.stdin.readline

N,K = map(int, input().split())
temperatures = list(map(int, input().split()))
psum = [temperatures[0]]
answer = -1e9

for i in range(N-1):
  psum.append(psum[i] + temperatures[i+1])

temp_sum = []

for i in range(N - K + 1):
  if i == 0 :
    sum = psum[i + K -1]
  else :
    sum = psum[ i + K - 1] - psum[i - 1]
  
  temp_sum.append(sum)

print(max(temp_sum))