import sys
input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    points.append( list(map(int, input().rstrip().split() ) ) )

points.sort(key=lambda x : (x[1], x[0]))

for point in points:
    print(*point)