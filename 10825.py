N = int(input())
students = []

for _ in range(N):
    a,b,c,d = list(map(str,input().split()))
    students.append( [a, int(b),int(c),int(d)])

students.sort(key = lambda x : (-x[1] , x[2],-x[3],x[0]) )

for s in students :
    print(s[0])