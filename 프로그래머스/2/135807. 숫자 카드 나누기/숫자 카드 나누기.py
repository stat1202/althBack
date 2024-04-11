import math

def  isNotDiv(array, a):
    for n in array:
        if n % a == 0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0
    a = arrayA[0]
    b = arrayB[0]
    flag = True
    for n in arrayA:
        a = math.gcd(n,a)
    for n in arrayB:
        b = math.gcd(n,b)
    
    if isNotDiv(arrayA, b):
        answer = max(answer, b)
        
    if isNotDiv(arrayB, a):
        answer = max(answer, a)
    return answer