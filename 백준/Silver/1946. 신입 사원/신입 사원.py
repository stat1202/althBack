import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  applicants = [list(map(int, input().split())) for _ in range(N) ]
  applicants.sort()

  interview_score = 1e9
  count = 0

  for i in range(N):
    if applicants[i][1] < interview_score:
      count += 1
      interview_score = applicants[i][1]

  print(count)
  