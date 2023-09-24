a, b, v = map(int, input().split() )


answer = (v-b) // (a-b)
if (v-b) % (a-b) == 0:
    print(answer)    
else:
    print(answer + 1)