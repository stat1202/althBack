import sys
input = sys.stdin.readline
n = input().rstrip()
count = 0
while len(n) > 1:
    tmp = 0
    count += 1
    for s in n:
        tmp += int(s)
    n = str(tmp)
print(count)

if int(n) % 3 == 0:
    print("YES")
else:
    print("NO")