from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque( map( int, input().split() ) )

    for i in range( len(queue) ):
        queue[i] = (queue[i], i)
    count = 0
    while queue:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == M:
                print(count)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())