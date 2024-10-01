def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]) )
    answer = 0
    for i in range(row_begin-1, row_end):
        s_i = 0
        for d in data[i]:
            s_i += d % (i+1)
        
        answer = answer ^ s_i
    
    return answer