for _ in range(5):
	k = input()
	a = 0
	x = 1
	for i  in range(len(k)):
		if i % 2 == 0:
			a += int(k[i])
		else:
			if int(k[i]) != 0:
				x *= int(k[i])
	a = a * x

	print(a % 10)
