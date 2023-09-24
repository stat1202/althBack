n = int(input())
nums = list(map(int, input().split(" ") ))

def isDecimal(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
        
# print(nums)
answer = 0

for num in nums:
    if isDecimal( num ):
        answer += 1
print(answer)
