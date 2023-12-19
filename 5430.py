from collections import deque
T = int(input())


for _ in range(T):
    p = input()
    n = int(input())
    data = input().lstrip("[").rstrip("]")
    nums =deque(list(data.split(","))) if data else deque([])
    flag = True
    r_flag = False
    
    if p.count("D") > len(nums):
        print("error")
        continue
        
    for command in p:
        if nums:
            if command == "R":
                r_flag = not r_flag
            elif command == "D":
                if r_flag:
                    nums.pop()
                else:
                    nums.popleft()
    if r_flag:
        nums.reverse()
        
    if flag:
        result = ",".join(nums)
        print(f'[{result}]')
