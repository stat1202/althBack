A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

sec = 0

if A < 0:
  sec += abs(A) * C + D + B * E
if A == 0:
  sec = D + B * E
if A > 0:
  sec = ( B - A )* E
print(sec)