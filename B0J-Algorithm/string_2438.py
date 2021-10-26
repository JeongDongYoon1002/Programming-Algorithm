# "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
# "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
# "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.

def solution(n, k, cmd):
    answer = []
    recent = []
    for i in range(n):
        answer.append('O')
    for i in range(len(answer)):
        recent[i] = answer[i]
    for i in range(len(cmd)):
        for j in range(len(cmd[i])):
            if cmd[i][j] == 'D':
                k = k - int(cmd[i][-1])
                break
            
            if cmd[i][j] == 'U':
                k = k + int(cmd[i][-1])
                break
            
            if cmd[i][j] == 'C':
                
                answer[k] = 'X'
                recent = k
                if k == n:
                    k = n - 1
                    n = n -1
                else:
                    k = k + 1
                    n = n - 1
                
                
                break
                

            if cmd[i][j] == 'Z':
                for i in range(answer):
                    answer[i] = recent[i]
                n = n + 1
                break
               

            

    return "".join(answer)

r = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
print(r)