from itertools import combinations

N, K = map(int, input().split())

V = [ input()[4:-4] for _ in range(N) ]

# anta tica a c i n t
words = []

if K < 5:
  print(0)
else:
  def solve(V, teach):
    count = 0
    for voca in V:
      possible = True
      for word in voca:
        if not teach[ord(word) - ord('a')]:
          possible = False
          break
      if possible:
        count += 1
    return count

  for i in range(26):
    if chr(ord('a') + i) in ['a', 'c', 'i', 'n', 't']:
      continue
    words.append(chr(ord('a') + i))

  teach = [False] * 26
  
  for a in ['a', 'c', 'i', 'n', 't']:
    teach[ord(a) - ord('a')] = True
  max_count = 0
  # print(words)

  for combination in combinations(words, K- 5):
    # print(combination)
    for a in combination:
      teach[ord(a) - ord('a')] = True
    
    count = solve(V, teach)
    max_count = max(max_count, count)

    for a in combination:
      teach[ord(a) - ord('a')] = False

  print(max_count)