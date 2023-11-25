s = input()

transform = s.replace('XXXX', 'AAAA').replace('XX', 'BB')

if 'X'in transform:
    print(-1)
else:
    print(transform)