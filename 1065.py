num = int(input())

h = 0
for i in range(1, num+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        h += 1 
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        h += 1
print(h)