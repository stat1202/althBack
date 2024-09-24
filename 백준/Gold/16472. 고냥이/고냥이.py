N = int(input())
S = input()

alphabet = [0] * 26
start = 0
end = 0

max_length = 0
alphabet[ord(S[0]) - ord('a')] = 1
count = 1

while start < len(S) and end < len(S):
  if count <= N:
    max_length = max(max_length, end - start + 1)
    end += 1

    if end < len(S):
      s_end = ord(S[end]) - ord('a')
      alphabet[s_end] += 1
      if alphabet[s_end] == 1:
        count += 1
  else:
    start += 1
    s_start = ord(S[start-1]) - ord('a')
    alphabet[s_start] -= 1
    if alphabet[s_start] == 0:
      count -= 1
print(max_length)