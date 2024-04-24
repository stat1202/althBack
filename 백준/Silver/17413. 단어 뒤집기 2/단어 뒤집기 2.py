import sys
input = sys.stdin.readline

S = input().rstrip()
answer = ""
stack = []
flag = False

for s in S:
    
    if s == " ":
        while stack:
            answer += stack.pop()
        answer += s
    elif s == "<":
        while stack:
            answer += stack.pop()
        flag = True
        answer += s
    elif s == ">":
        flag = False
        answer += s
    elif flag:
        answer += s
    else:
        stack.append(s)
while stack:
    answer += stack.pop()
print(answer)
    