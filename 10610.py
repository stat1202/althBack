nums = list(input())
nums.sort(reverse= True)
rest = 0 
for n in nums:
    rest += int(n)
if rest % 3 == 0 and nums[-1] == "0":
    print("".join(nums))
else:
    print(-1)