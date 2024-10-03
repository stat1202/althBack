def solution(cards):
    answer = []
    cards = [card - 1 for card in cards]
    visited = [False] * len(cards)
    prev_l = 0
    for i in range(len(cards)):
        if not visited[i]:
            dfs(i, visited, cards)
            
            answer.append( len( list(filter(lambda x: x ,visited) ) ) - prev_l )
            prev_l = len( list(filter(lambda x: x ,visited) ) )
    
    answer.sort()
    
    if len(answer) < 2:
        return 0
    else:
        return answer[-1] * answer[-2]

def dfs(v, visited, cards):
    visited[v] = True
    if not visited[ cards[v] ]:
        dfs( cards[v], visited, cards )
    