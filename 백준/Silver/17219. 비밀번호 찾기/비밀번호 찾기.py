import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split() )

notes = {}
for _ in range(N):
    addr, pw = input().rstrip().split()
    notes[addr] = pw

for _ in range(M):
    sites = input().rstrip()
    print( notes[sites] )