import sys
input = sys.stdin.readline

N = int(input())
datas = [ list(map(int, input().rstrip().split())) for _ in range(N) ]
items = []

for i in range(N):
	d = datas[i][0]/datas[i][1]
	items.append( (d, datas[i][0], i+1 ) )
	
items.sort( key = lambda x : (-x[0], -x[1], x[2]) )
print(items[0][2])
