import math
n = int(input())
S = str( math.factorial(n) )
answer = 0
for i in range(len(S)-1, -1, -1):
    if S[i] == "0":
        answer += 1
    else:
        break
print(answer)