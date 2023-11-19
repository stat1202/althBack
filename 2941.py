s = input()

d = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in d :
    s = s.replace(c, '*')
print(len(s))


