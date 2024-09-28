from collections import Counter

s = input().upper()
sets = list(set(s))

count = []
for i in sets:
    count.append( s.count(i) )
if count.count(max(count) ) > 1:
    print("?")
else:
    print( sets[ (count.index(max(count)))])
    
    