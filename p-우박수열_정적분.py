def seq(k):
    result = [k]
    while result[-1] > 1:
        if result[-1] % 2 == 1:
            a = result[-1]*3 + 1
            result.append(a)
        else:
            a = result[-1]/2
            result.append(a)
    return result
    
def calc_dimension(a,b):
    return (a+b) / 2
    
def solution(k, ranges):
    dimensions = []
    answer = []
    seqs = seq(k)
    n = len(seqs)
    for i in range(1, len(seqs)):
        a = calc_dimension(seqs[i], seqs[i-1] )
        
    for r in ranges:
        s,e = r
        x = n + e
        if s >= x:
            answer.append(-1)
        else:
            d = 0
            for i in range(s+1,x):
                d += calc_dimension(seqs[i], seqs[i-1] )
            answer.append(d)
    return answer
