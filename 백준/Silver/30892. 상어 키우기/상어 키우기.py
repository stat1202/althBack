from queue import PriorityQueue
N, K, T = map(int, input().split())

sharks = list( map(int, input().split()) )

sharks.sort()
pq = PriorityQueue()

pos = 0

for _ in range(K):
  while pos < N and sharks[pos] < T:
    pq.put(-sharks[pos])
    pos += 1

  if pq.qsize() == 0:
    break

  T += -pq.get()

print(T)
