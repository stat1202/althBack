# 배달해야하는 kg N

N = int( input() )

max_5 = N//5

answer = []
for i in range(max_5+1):
    weights_5 = 5 * i
    rest_weights = N - weights_5
    
    if rest_weights % 3 == 0:
        total_count = i + rest_weights//3
        answer.append(total_count)
        total_count = 0
if answer:
    print(min(answer))
else:
    print(-1)
