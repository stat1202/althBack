N = int(input())
results = [N]
count = 0
if N == 1:
    print(0)
else:
    while True:
        tmp = []
        for n in results:
            if n % 3 == 0 :
                tmp.append(n//3)
            if n % 2 == 0 :
                tmp.append(n//2)
            tmp.append(n-1)
        results = tmp
        count += 1
        if 1 in results:
            break
    print(count)