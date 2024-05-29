# 1. graph[i][j]와 graph[i+n][j+n]이 일치하는 숫자를 기록
# [ [(p1,p2),[(a,b), (c,d)...] ] ]
# 2. 각 조합에서 직사각형 인 것 찾기 graph[p1][b] graph[a][p2]가 같은 숫자인지 판단
# 같다면 길이 추가
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
  data = list(map(int, list(input().rstrip())))
  graph.append(data)

square_candidates = []

for i in range(n):
  for j in range(m):
    for k in range(1,n):
      if (0<= i+k < n and 0<= j+k < m) and  graph[i][j] == graph[i+k][j+k]:
        square_candidates.append([(i,j), (i+k, j+k)])

result = 0

for cand in square_candidates:
  p1, p2 = cand
  p3 = (p1[0], p2[1])
  p4 = (p2[0], p1[1])
  target = graph[p1[0]][p1[1]]
  # print(p1, p2,p3, p4)
  if target == graph[p3[0]][p3[1]] and target == graph[p4[0]][p4[1]]:
    result = max(abs(p2[0] - p1[0]), result)
print( (result+1)**2)