from collections import deque

n, k = map(int,input().split() )

circle = deque( [i for i in range(1, n+1)] )
answer = []

while circle:
    circle.rotate(-(k-1))
    answer.append( circle.popleft() )
print("<", end="")
for i in range(len(answer) ):
    if i < len(answer) -1:
        print(f"{answer[i]}, ", end="")
    elif i == len(answer) -1:
        print(f"{answer[i]}", end="")
print(">")