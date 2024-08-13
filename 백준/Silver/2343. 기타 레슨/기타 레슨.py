import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

left = max(lectures)
right = sum(lectures)
answer = -1

while left <= right:
  middle = (left + right) // 2

  blueray_num = 1
  remain = middle

  for i in range(N):
    if remain < lectures[i]:
      blueray_num += 1
      remain = middle
    
    remain -= lectures[i]

  if blueray_num <= M :
    answer = middle
    right = middle - 1
  else:
    left = middle + 1
  
print(answer)