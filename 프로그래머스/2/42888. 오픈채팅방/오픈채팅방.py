def solution(record):
    answer = []
    tmp = []
    dic = {} 
    
    def order(rec):
        if rec[0] == "Enter":
            tmp.append(['e', rec[1]])
            dic[rec[1]] = rec[2]
        elif rec[0] == "Leave":
            tmp.append(['l', rec[1]])
        else:
            dic[rec[1]] = rec[2]
        return
            
    for rec in record:
        order(rec.split())
      
    for t, r in tmp:
        if t == 'e':
            answer.append(f'{dic[r]}님이 들어왔습니다.')
        else:
            answer.append(f'{dic[r]}님이 나갔습니다.')

    return answer
