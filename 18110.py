import sys
input = sys.stdin.readline

n = int(input())

if n!=0:
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    x = round(n*0.15+0.0000001);
    s = sum(arr[x:n-x])
    answer = round( (s/(n-2 * x)) + 0.0000001 ) 
    print(answer)
else:
    print(0)