data = []
for i in range(1,9):
    data.append([int( input()), i ] )
data.sort(reverse=True)

problem_scores = list( map(lambda x : x[0], data[0:5]) )
problem_nums = list( map(lambda x : x[1], data[0:5]) )
problem_nums.sort()
print(sum(problem_scores))
print( *problem_nums )