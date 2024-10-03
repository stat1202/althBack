N = int(input())
parent = list( map(int, input().split(" ")) )
D = int(input())

def dfs(n):
  parent[n] = -10
  for i in range(N):
    if n == parent[i]:
      dfs(i)

dfs(D)

answer = 0
for i in range(N):
  if parent[i] != -10 and i not in parent:
    answer += 1
print(answer)
