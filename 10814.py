import sys
input = sys.stdin.readline
n = int(input())

users = []
for i in range(n):
    age, name = input().rstrip().split()
    age = int(age)
    users.append( [age, i, name])
users.sort()
for user in users:
    print(f'{user[0]} {user[2]}')
