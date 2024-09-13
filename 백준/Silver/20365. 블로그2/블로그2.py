from collections import Counter
N = int(input())
S = input()

posts = []

for s in S:
  if posts:
    if posts[-1] != s:
      posts.append(s)
  else:
    posts.append(s)
counts = Counter(posts)
print( min( counts['B'], counts['R'] ) + 1 )