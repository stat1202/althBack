R, C = map(int, input().split())
B = [input() for _ in range(R)]

answer = 0
check = [False] * 26

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c, count):
  global answer
  answer = max(answer, count)
  for i in range(4):
    nr, nc = r + dr[i], c + dc[i]

    if 0 <= nr < R and 0 <= nc < C and not check[ord(B[nr][nc]) - ord('A')]:
      check[ord(B[nr][nc]) - ord('A')] = True
      dfs(nr, nc, count + 1)
      check[ord(B[nr][nc]) - ord('A')] = False

check[ord(B[0][0]) - ord('A')] = True
dfs(0, 0, 1)

print(answer)