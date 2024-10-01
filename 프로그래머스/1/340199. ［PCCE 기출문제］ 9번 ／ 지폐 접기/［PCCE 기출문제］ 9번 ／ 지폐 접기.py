def solution(wallet, bill):
    wallet.sort()
    # [작은값, 큰 값]
    answer = 0
    bill.sort()
    
    if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
        return 0
    
    while True:
        
        bill[1] //= 2
        bill.sort()
        answer += 1
        
        if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
            break
    return answer