n = int(input())
datas = [input() for _ in range(n) ]

datas = list(set(datas))
datas.sort()
datas.sort(key=len)
for d in datas:
    print(d)