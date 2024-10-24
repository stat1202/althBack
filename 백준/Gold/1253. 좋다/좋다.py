# 2200

n = int(input() )
nums = list( map(int, input().split()) )
nums.sort()

count = 0

for i in range(n):
    start = 0
    end = n-1

    while start < end:
        t = nums[start] + nums[end] 
        if t == nums[i]:
            if i == start:
                start += 1
            elif i == end:
                end -=1
            else:
                count += 1
                break
        elif t > nums[i]:
            end -= 1
        else:
            start += 1
print( count )
                