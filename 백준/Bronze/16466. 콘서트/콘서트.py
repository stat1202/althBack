import sys
input = sys.stdin.readline

N = int(input())

tickets = [False] * 1000000

for i in list(map(int, input().split())):
  tickets[i-1] = True



for i in range(len(tickets)):
  if not tickets[i]:
    print( i + 1 )
    break