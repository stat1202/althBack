from collections import deque

A, B = map(int, input().split())

def AtoB(A,B):
    q = deque([(A, 0)])
    visited = set()
    
    while q:
        current, count = q.popleft()
        if current == B:
            return count+1
        next_double = current * 2
        if next_double <= 10**9 and next_double not in visited:
            visited.add(next_double)
            q.append((next_double, count + 1))

        next_append_one = current * 10 + 1
        if next_append_one <= 10**9 and next_append_one not in visited:
            visited.add(next_append_one)
            q.append((next_append_one, count + 1))
    return -1
print(AtoB(A,B))