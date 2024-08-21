N = int(input())

str_N = str(N)

digit = len(str_N)

count = 0
for i in range(1, digit):
  count += 9 * i * 10 ** (i-1)

count +=  (N - 10**(digit-1) + 1) * digit
print(count)