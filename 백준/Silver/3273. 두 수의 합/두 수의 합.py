n = int(input() )
nums = list(map(int, input().split() ))
goal = int(input())
nums.sort()
s = 0
e = n-1
answer = 0
while s < e:
    if nums[s] + nums[e] > goal:
        e -= 1
    elif nums[s] + nums[e] == goal:
        s += 1
        e -= 1
        answer += 1
    else:
        s+= 1
print(answer)