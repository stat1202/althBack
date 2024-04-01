def solution(s):
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
    
    return False if stack else True