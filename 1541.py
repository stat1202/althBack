import sys
input = sys.stdin.readline

data = input().rstrip()
split_data = data.split("-")

# print(data)
answer = []
for d in split_data:
    tmp = d.split("+")
    answer.append( sum( map(int, tmp) ) )

if data[0] == "-":
    print(-sum(answer))
else:
    print( -1 *( sum(answer[1:]) - answer[0] ) )
    
    