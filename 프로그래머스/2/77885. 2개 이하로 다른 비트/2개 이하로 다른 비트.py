def find_bit(n):
    a = list("0" + bin(n)[2:])
    i = "".join(a).rfind("0")
    a[i] = "1"
    if n % 2 != 0:
        a[i+1] = "0"
        
    return int("".join(a), 2)

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(find_bit(n))
    return answer