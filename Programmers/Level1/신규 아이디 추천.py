def solution(new_id):
    answer = ''
    
    #1 단계
    new_id = new_id.lower()
    
    #2 단계
    for value in new_id:
        if value.islower() or value.isdigit() or value in ["-", "_", "."]:
            answer += value
            
    # 3단계
    
    while '..' in answer:
        answer = answer.replace('..', '.')
        print(answer)
    
    # 4단계
    if answer[0] == ".":
        if len(answer) >= 2:
            answer = answer[1:]
        else:
            answer ="."
    if answer[-1] == ".":
        answer = answer[:-1]
    
    #5 단계
    if answer == "":
        answer = "a"
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer
