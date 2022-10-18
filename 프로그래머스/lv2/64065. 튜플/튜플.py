def solution(s):
    answer = []
    ans_tmp = []
    num = ''
    for i in range(1, len(s)-1):
        if s[i] == '{':
            tmp = []
            
        elif s[i] == '}':
            tmp.append(int(num))
            num = ''
            ans_tmp.append(tmp[:])
            tmp = []
            
        elif s[i] == ',':
            if num:
                tmp.append(int(num))
                num = ''
            else:
                pass
            
        else:
            num += s[i]
    ans_tmp.sort(key=lambda x:len(x))
    for i in ans_tmp:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer