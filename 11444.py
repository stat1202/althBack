import sys
input = sys.stdin.readline

def power(adj, n):
    if n == 1:
        return adj
    elif n%2 == 0:
        return power(multi(adj, adj), n //2)
    else:
        return multi(power(adj, n-1), adj)
def multi(a,b):
    tmp = [[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            s = 0
            for k in range(2):
                s += a[i][k]*b[k][j]
            tmp[i][j] = s%1000000007
    return tmp
    
n = int(input())

adj = [[1,1],[1,0]]
start = [[1],[1]]
if n < 3:
    print(1)
else:
    print(multi(power(adj,n-2),start)[0][0])