data = [0]*11
data[0] = 1
data[1] = 2
data[2] = 4

for i in range(3,11):
    data[i] = data[i-1] + data[i-2] + data[i-3]
T = int(input())
for _ in range(T):
    N = int(input())
    print(data[N-1])