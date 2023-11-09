import sys
input = sys.stdin.readline

N = int( input() )

papers = [ list( map(int, input().rstrip().split() ) ) for _ in range(N) ]
print(papers)

        