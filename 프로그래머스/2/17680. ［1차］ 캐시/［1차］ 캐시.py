from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        c = city.lower()
        
        if c in cache:
            answer += 1
        else:
            answer += 5
        
        if c in cache:
            cache.remove(c)
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
        cache.append(c)
    return answer