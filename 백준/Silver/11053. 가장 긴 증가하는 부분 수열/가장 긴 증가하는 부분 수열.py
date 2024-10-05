import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().rstrip().split()))
counts = [0]*N

for i in range(N):
    count = 0
    for j in range(0, i):
        if nums[j] < nums[i]:
            count = max(count, counts[j])
        
    counts[i] = count + 1
print(max(counts))
        
    