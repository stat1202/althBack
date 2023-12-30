import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

words = set()
answer = 0
for _ in range(N):
    word = input().rstrip()
    words.add(word)
for _ in range(M):
    s =  input().rstrip()
    if s in words:
        answer += 1
print(answer)