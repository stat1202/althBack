def solution(s):
    stack = []
    
    for i in s:
        if stack:
            if i == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    return True if not stack else False
