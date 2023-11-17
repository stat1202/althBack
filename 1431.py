import sys
input = sys.stdin.readline

guitars = []
N = int(input())

def sum_serial(serial):
    result = 0
    for s in serial:
        if s.isdigit():
            result += int(s)
    return result

for _ in range(N):
    guitars.append( input().rstrip() )
    
guitars.sort(key = lambda x: (len(x), sum_serial(x), x ))

for guitar in guitars:
    print(guitar)