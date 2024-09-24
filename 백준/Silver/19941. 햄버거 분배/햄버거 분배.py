from queue import PriorityQueue
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = input().rstrip()
pq = PriorityQueue()

for i in range(N):
  if S[i] == "H":
    pq.put(i)

count = 0

for i in range(N):
  if S[i] == "P":
    while pq.qsize() > 0:
      x = pq.get()

      if abs(x - i) <= K:
        count += 1
        break

      if x < i :
        continue
      else:
        pq.put(x)
        break
print(count)