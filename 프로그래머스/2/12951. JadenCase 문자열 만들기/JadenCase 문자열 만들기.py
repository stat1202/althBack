def solution(s):
    jaden = s.split(" ")
    answers = []
    for j in jaden:
        answers.append( j.capitalize() )
        
    return " ".join(answers)
