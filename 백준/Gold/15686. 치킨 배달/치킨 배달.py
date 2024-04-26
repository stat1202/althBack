# N 도시 크기 M 치킨집 최대 개수
# 2<= N <= 50 1<= M <= 13
# 2150
from itertools import combinations
N, M = map(int, input().split())
maps = [ input().split() for _ in range(N)]

# print(N,M)
# print(maps)

one_arr = []
two_arr = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == "1":
            one_arr.append([i,j])
        elif maps[i][j] == "2":
            two_arr.append([i,j])
combs =  list( combinations(two_arr, M) )
answers = []
for comb in combs:
    d = 0
    for one in one_arr:
        min_dist = 1000
        for store in comb:
            dist = abs(store[0]-one[0]) + abs(store[1]-one[1])
            if dist < min_dist:
                min_dist = dist
        d += min_dist
    answers.append(d)
print(min(answers) )