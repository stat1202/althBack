import sys

input = sys.stdin.readline

N, K, B = map(int, input().split())
traffic_lights = [1]*N

for _ in range(B):
  i = int(input())
  traffic_lights[i-1] = 0

psum = [traffic_lights[0]]
for i in range(N-1):
  psum.append(psum[i] + traffic_lights[i+1])
  
traffic_sum = []

for i in range(N - K):
  traffic_sum.append(psum[i + K] - psum[i])

print( K - max(traffic_sum) )