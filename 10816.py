import sys
input = sys.stdin.readline
from collections import Counter
n = int( input() )
nums = list(map(int, input().rstrip().split()))
c = Counter(nums)
# print(c)
m = int( input() )
nums2 = list(map(int, input().rstrip().split()))

for i in nums2:
    print( c[i], end=" ")