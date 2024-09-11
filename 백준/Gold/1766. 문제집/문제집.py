from queue import PriorityQueue

N, M = map(int, input().split())

adj = [ [] for _ in range(N)]
problems = [0] * N

for _ in range(M):
  a, b = map(int, input().split())
  adj[a-1].append(b-1)
  problems[b-1] += 1

problem_order = []
pq = PriorityQueue()

for i in range(N):
  if problems[i] == 0:
    pq.put(i)

while pq.qsize() != 0:
  v = pq.get()
  problem_order.append(v)

  for n in adj[v]:
    problems[n] -= 1
    if problems[n] == 0:
      pq.put(n)

for o in problem_order:
  print(o+1, end=" ")