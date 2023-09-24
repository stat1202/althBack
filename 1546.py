n = int(input())
scores = list(map(int, input().split(" ")))
# print(scores)
new_scores = [ score/max(scores) * 100 for score in scores]
print( sum(new_scores) / n )