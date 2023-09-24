while True:
    data = input()
    num = list(data)
    if data == "0":
        break

    r_num = list(reversed(num))
    flag = True
    for i in range(len(num)):
        if num[i] != r_num[i]:
            flag = False
            break
    if flag:
        print("yes")
    else:
        print("no")