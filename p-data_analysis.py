def extraction(data, ext, val_ext):
    result = []
    for d in data:
        if ext == "code" and d[0] < val_ext:
            result.append(d)
        elif ext == "date" and d[1] < val_ext:
            result.append(d)
        elif ext == "maximum" and d[2] < val_ext:
            result.append(d)
        elif ext == "remain" and d[3] < val_ext:
            result.append(d)
    return result
def sort_data (data, sort_by):
    if sort_by == "code":
        data.sort( key = lambda x: x[0])
    elif sort_by == "date":
        data.sort( key = lambda x: x[1])
    elif sort_by == "maximum":
        data.sort( key = lambda x: x[2])
    elif sort_by == "remain":
        data.sort( key = lambda x: x[3])
        
    return data

def solution(data, ext, val_ext, sort_by):
    a = extraction(data, ext, val_ext)
    answer = sort_data(a, sort_by)
    return answer
