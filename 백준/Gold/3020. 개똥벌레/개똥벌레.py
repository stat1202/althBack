def solution(N, H, obstacles):
    stalactites = [0] * (H + 1)
    stalagmites = [0] * (H + 1)
    
    for i in range(N):
        if i % 2 == 0:
            stalactites[obstacles[i]] += 1
        else:
            stalagmites[obstacles[i]] += 1
    
    for i in range(H - 1, 0, -1):
        stalactites[i] += stalactites[i + 1]
        stalagmites[i] += stalagmites[i + 1]
    
    min_obstacles = N // 2
    count = 0
    
    for i in range(1, H + 1):
        total_obstacles = stalactites[i] + stalagmites[H - i + 1]
        
        if total_obstacles < min_obstacles:
            min_obstacles = total_obstacles
            count = 1
        elif total_obstacles == min_obstacles:
            count += 1
    
    return min_obstacles, count

# 입력 받기
N, H = map(int, input().split())
obstacles = []
for _ in range(N):
    obstacles.append(int(input()))

# 문제 해결 함수 호출
min_obstacles, count = solution(N, H, obstacles)

# 결과 출력
print(min_obstacles, count)