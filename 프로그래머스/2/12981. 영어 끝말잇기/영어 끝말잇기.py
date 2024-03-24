def solution(n, words):
    words_arr = []
    
    for i in range(len(words)):
        word = words[i]
        
        if not words_arr:
            words_arr.append(word)
        elif word in words_arr:
            return [i%n + 1, i//n + 1]
        elif words_arr[-1][-1] != word[0]:
            return [i%n + 1, i//n + 1]
        else:
            words_arr.append(word)

    return [0,0]