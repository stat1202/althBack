from collections import deque

def isValid(s):
    stack = []
    for i in s:
        # print("i", stack)
        if stack:
            a = stack[-1]
            if a == "(" and i==")":
                stack.pop()
            elif a == "[" and i=="]":
                stack.pop()
            elif a == "{" and i=="}":
                stack.pop()
            elif i == "(" and i == "[" and i == "{":
                stack.append(i)
            else:
                stack.append(i)
        else:
            stack.append(i)
    # print(stack)
    return True if not stack else False

def solution(s):
    s = deque(s)
    answer = 0
    
    for i in range(len(s)):
        s.rotate(-1)
        if isValid(s):
            answer += 1
    
    return answer