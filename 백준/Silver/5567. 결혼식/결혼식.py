n = int(input())
m = int(input())

graph = [ [] for _ in range(n)]
visited = [0] * n

for _ in range(m):
  a, b = map(int,input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

friend = [0] * n
friend_of_friend = [0] * n

for node in graph[0]:
  friend[node] = 1

for i in range(n):
  if friend[i] == 1:
    for node in graph[i]:
      if node != 0 and friend[node] != 1:
        friend_of_friend[node] = 1

print( sum(friend) + sum(friend_of_friend))