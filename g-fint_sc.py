t = int(input())
for _ in range(t):
	n = int(input())
	scores = list(map(int,input().split()))
	avg = sum(scores) / n
	p = 0
	for s in scores:
		if s >= avg:
			p += 1
	print(f"{p}/{n}" )
		
