import heapq
import sys
input = sys.stdin.readline

T = int(input())

def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    nums = dict()
    
    for _ in range(k):
        command, num = input().rstrip().split()
        num = int(num)
        
        if command == "I":
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
        elif command == "D":
            if not isEmpty(nums.items()):
                if num == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        tmp = -heapq.heappop(max_heap)
                        
                        if tmp in nums:
                            del(nums[tmp])
                    nums[-max_heap[0]] -= 1
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        tmp = heapq.heappop(min_heap)
                        if tmp in nums:
                            del(nums[tmp])
                    nums[min_heap[0]] -= 1
    if isEmpty(nums.items()):
        print("EMPTY")
    else:
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        print(-max_heap[0], min_heap[0])
