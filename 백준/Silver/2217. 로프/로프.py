N = int(input())

ropes = [ int(input()) for _ in range(N) ]

sorted_ropes = sorted(ropes, reverse=True)
max_weights = 0

while sorted_ropes:
  w  = sorted_ropes.pop()
  max_weights = max( w * (len(sorted_ropes) + 1), max_weights)

print(max_weights)