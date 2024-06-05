from itertools import combinations

N,M=map(int,input().split())
nums = list(combinations([i for i in range(1,N+1)],M))

for i in nums:
    answer = ""
    for j in i:
        answer +=str(j)
        answer +=" "
    print(answer)