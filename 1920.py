import sys
input = sys.stdin.readline

a = {}
n = int(input())
nums = list( map(int, input().rstrip().split())) 
nums.sort()
m = int(input())
nums2 = list( map(int, input().rstrip().split())) 

for num in nums2:
    start = 0
    end = n-1
    mid = (start + end) // 2
    flag = False
    
    while start < end:
        if nums[mid] > num:
            end = mid-1
            mid = (start + end) // 2
        elif nums[mid] < num:
            start = mid+1
            mid = (start + end) // 2
        else:
            flag = True
            break
    if  nums[mid] == num or nums[start] == num or nums[end] == num:
        flag = True
    if flag:
        print(1)
    else:
        print(0)
    