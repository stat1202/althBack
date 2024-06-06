N,M = map(int, input().split(" "))

packages = []
singles = []

cost = 0

for _ in range(M):
  p, s = map(int, input().split(" "))
  packages.append(p)
  singles.append(s)

packages.sort()
singles.sort()

buy_package = N // 6
buy_single = N%6

if packages[0] < singles[0]*6:
  cost += packages[0]* buy_package
else:
  cost += singles[0]* buy_package*6

if packages[0] < singles[0]* buy_single:
  cost += packages[0]
else:
  cost += singles[0]*buy_single
print(cost)