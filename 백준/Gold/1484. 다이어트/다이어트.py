G = int(input())

A = [i * i for i in range(100001) ]

start = 1
end = 2
answer = []

while True:
  # A[end] - A[start] < G end 증가
  
  if A[end] - A[start] < G:
    end += 1
  
  elif A[end] - A[start] == G:
    answer.append(end)
    start += 1

  else:
    start += 1

  if end == 100000 and A[end] - A[start] < G:
    break


if answer:
  for a in answer:
    print(a)  
else:
  print(-1)