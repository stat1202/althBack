import sys
input = sys.stdin.readline

n, m = map(int, input().split() )

group = set()
answer = []

for _ in range(n):
    group.add( input().strip() )

for _ in range(m):
    compare = input().strip()
    if compare in group:
        answer.append(compare)

answer.sort()
print(len(answer))
for an in answer:
    print(an)