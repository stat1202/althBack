word = input()
answers = []
for i in range(0,len(word)):
    answers.append(word[i:])
answers.sort()

for answer in answers:
    print(answer)