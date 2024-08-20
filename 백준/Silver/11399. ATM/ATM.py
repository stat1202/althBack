import sys
input = sys.stdin.readline

N = int(input())
lines = sorted(list(map(int, input().split())))

answer = [0]

for i in range(N):
  answer.append(answer[i] + lines[i])
print(sum(answer))