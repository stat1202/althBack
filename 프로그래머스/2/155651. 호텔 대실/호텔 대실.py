def solution(book_time):
    t_book_time = []
    end_time = []
    answer = 0
    
    for b in book_time:
        s_h, s_m = b[0].split(":")
        e_h, e_m = b[1].split(":")
        
        t_book_time.append( (int(s_h)* 60 + int(s_m), int(e_h)* 60 + int(e_m)) )
        
    t_book_time.sort()
    
    for b in t_book_time:
        s,e = b
        if not end_time:
            end_time.append(e)
            answer += 1
        else:
            for i in range(len(end_time)):
                if end_time[i] + 10 <= s:
                    end_time[i] = e
                    break
            else:
                end_time.append(e)
                answer += 1
            
        
    return answer