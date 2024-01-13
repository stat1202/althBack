import sys
input = sys.stdin.readline

N, K = map(int, input().split())

temperatures = list(map(int, input().split()))
start = 0
end = start + K
answer = -1e9
s = sum(temperatures[start:end])
answer = max( s, answer)
while end < N:
    s = s - temperatures[start] + temperatures[end]
    answer = max( s, answer)
    start += 1
    end += 1

print(answer)