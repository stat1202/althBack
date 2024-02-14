n, k = map(int, input().split())
nums = input().split()
count = 0

for n in nums:
	if not str(k) in n:
		count += 1
print(count)
