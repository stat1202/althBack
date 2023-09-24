n = int( input() )
nums = [ list( map(int, input().split() ) ) for _ in range(n) ]
nums.sort()

for num in nums:
    print(*num)

