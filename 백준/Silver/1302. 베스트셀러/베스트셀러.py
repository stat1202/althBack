from collections import Counter
N = int(input())

books = []

for _ in range(N):
  books.append(input())
sales = Counter(books).most_common()
sales.sort(key= lambda x: (-x[1],x[0]), reverse=True)
print(sales[-1][0])