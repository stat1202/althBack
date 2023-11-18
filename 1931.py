import sys
input = sys.stdin.readline

N = int(input())
answer = 0
times = []

for _ in range(N):
    times.append(list(map(int, input().rstrip().split(" "))))
times.sort(key=lambda x: (x[1], x[0]))

end_time = 0
for time in times:
    start, end = time
    if start >= end_time:
        end_time = end
        answer += 1
# print(times)
print(answer)