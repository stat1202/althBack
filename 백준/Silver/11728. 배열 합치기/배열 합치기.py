import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

composition_list = A+B

composition_list.sort()
print(*composition_list)

