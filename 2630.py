from collections import deque
import sys
input = sys.stdin.readline

N = int( input() )

papers = [ list( map(int, input().rstrip().split() ) ) for _ in range(N) ]
queue = deque([papers])

while queue:
    paper = queue.popleft()
    l = len(paper)
    stack = [paper[0][0]]
    flag = False
    for i in range(l):
        for j in range(1,l):
            if paper[i][j] != stack[-1]:
                
    
    