from collections import deque
import itertools

def solution(prices):
    d_prices = deque(prices)
    result = []
    
    while d_prices:
        price = d_prices.popleft()
        if d_prices:
            # if price <= min(d_prices):
            #     result.append( len(d_prices) )
            # else:
            count = 0
            for i in d_prices:
                if i >= price:
                    count += 1
                else:
                    count += 1
                    break
            result.append( count )
                
    result.append(0)
    return result

