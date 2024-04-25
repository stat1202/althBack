# 2130
# 블록 제거 후 블록 1 증가 2초
# 블록 놓기 1초
from collections import Counter

N,M, blocks = map(int, input().split() )

maps = []
for _ in range(N):
    inputs = list(map(int, input().split()))
    maps += inputs
    
counters = Counter(maps)
result = []
for i in range(257):
    # i 목표 높이
    tmp_time = 0
    del_blocks = 0
    stack_blocks = 0
    for c in counters:
        # c -> counters key c > i 보다 크다면 지워야함
        n = counters[c] # 높이가 c인 블록의 개수
        if c > i :
            del_blocks += n * (c-i)
        elif c == i:
            continue
        else:
            stack_blocks += n * (i-c)
    if del_blocks + blocks >= stack_blocks:
        tmp_time += ( del_blocks * 2 + stack_blocks)
        result.append( [ tmp_time, i] )
        # print(i)

result.sort(key= lambda x: (x[0], -x[1]) )
# 
# print(len(result) )
print( result[0][0], result[0][1])
# 지워야할 블록 개수 del_blocks
# 쌓아야할 블록 개수 stack_blocks2