import sys
input = sys.stdin.readline

nameToNum = {}
numToName = {}

N,M = map(int, input().rstrip().split())

for i in range(1,N+1):
    data = input().rstrip()
    nameToNum[data ] = i
    numToName[i] = data
    
for _ in range(M):
    search = input().rstrip()
    if search in nameToNum.keys() :
        print(nameToNum[search])
    else:
        print(numToName[int(search)s])
