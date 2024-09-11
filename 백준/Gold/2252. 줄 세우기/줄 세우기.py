from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
adj = [ [] for _ in range(N) ]

counts = [0] * N

for _ in range(M):
  a, b = map(int, input().split())
  adj[a-1].append(b-1)
  counts[b-1] += 1

heights = []
q = deque([])

for i in range(N):
  if counts[i] == 0:
    q.append(i)

while q:
  v = q.popleft()
  heights.append(v)

  for n in adj[v]:
    counts[n] -= 1
    if counts[n] == 0:
      q.append(n)

for h in heights:
  print( h+1, end=" ")