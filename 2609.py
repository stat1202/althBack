a,b = map(int, input().split())
nums = []
count = 2
while count <= min(a,b):
    if a % count == 0 and b % count == 0 :
        nums.append(count)
        a //= count
        b //= count
    else:
        count += 1
# print(nums, a, b)
answer = 1
for n in nums:
    answer *= n
print(answer)
answer *= a*b
print(answer)