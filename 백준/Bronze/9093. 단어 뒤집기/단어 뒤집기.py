T = int(input())

for _ in range(T):
  S = input().split(" ")
  for i in range(len(S)):
    S[i] = S[i][::-1]
  print(" ".join(S))