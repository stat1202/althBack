from itertools import combinations
n, m = map(int, input().split())
nums = list( map(int, input().split()) )
comb = list( combinations(nums,3) )
comb = list(map(sum, comb))
comb.sort()

answer = 0
for c in comb:
    if c > m:
        break
    answer = c
print(answer)