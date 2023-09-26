n = int(input())

datas = []
for _ in range(n):
    d = list( map(int, input().split()) )
    datas.append(d)
answer = []

for i in range(n):
    data = datas[i]
    tmp = datas[:i] + datas[i+1:]
    count = 0
    for t in tmp:
        if data[0] < t[0] and data[1] < t[1]:
            count += 1
    answer.append(count+1)
print(*answer)