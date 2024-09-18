import heapq

N = int(input())
heap = []

for _ in range(N):
  a = list(map(int, input().split()))

  for j in a:
    if len(heap) < N:
      heapq.heappush(heap, j)
    else:
      if heap[0] < j:
        heapq.heappush(heap, j)
        heapq.heappop(heap)

print(heap[0])