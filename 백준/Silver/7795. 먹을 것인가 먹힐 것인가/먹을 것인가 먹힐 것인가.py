# 2130

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    # print(A, B)
    count = 0
    total = 0
    # A와 B 원소 비교
    # A가 B보다 크면 축적 -> B 크기 키우기
    # B 끝에 오거나 A가 B보다 작아지면 총 개수 증가
    for i in range(N):
        while True:
            if count == M or A[i] <= B[count]:
                total += count
                break
            else:
                count += 1
    print(total)
