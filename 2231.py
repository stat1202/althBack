n = int(input())

answer = 0
for i in range(1,n+1):
    compare = i
    nums = list( str(i) )
    sums = 0
    for num in nums:
        sums += int(num)
    if compare + sums == n:
        answer = compare
        break
print(answer)
