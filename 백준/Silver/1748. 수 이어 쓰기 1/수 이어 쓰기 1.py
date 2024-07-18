import sys
n = input().rstrip()
c = len(n)-1
answer = 0

for i in range(c):
    answer += 9 * (10 ** i) * (i+1)
    i += 1
answer += ( (int(n) -(10 ** c)) + 1) * (c+1)
print(answer)