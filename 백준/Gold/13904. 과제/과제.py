import heapq

N = int(input())

day = 0
assignments = []
score = 0

for _ in range(N):
  d, w =  map(int, input().split())
  day = max(d, day)
  heapq.heappush(assignments, (-d, -w) )

for i in range(day, 0, -1):
  tmp = []
  cand = []
  while assignments:
    d, w = heapq.heappop(assignments)
    
    if -d >= i:
      cand.append( (-w,-d) )
    else:
      tmp.append((d,w))
  
  cand.sort()
  
  if cand:
    score += cand.pop()[0]

  for t in tmp:
    heapq.heappush(assignments, t)
  
  for c in cand:
    heapq.heappush(assignments, (-c[1], -c[0]))

print(score)



