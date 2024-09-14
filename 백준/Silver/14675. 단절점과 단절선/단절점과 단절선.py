import sys
input = sys.stdin.readline

N = int(input())

bridges = []
adj = [ [] for _ in range(N) ]

for _ in range(N-1):
  a, b = map(int, input().split())
  adj[a-1].append(b-1)
  adj[b-1].append(a-1)

q = int(input())

for _ in range(q):  
  t, k = map(int, input().split())

  if t == 1:
    if len(adj[k-1]) == 1:
      print('no')
    else:
      print('yes')
  elif t == 2:
    print('yes')

