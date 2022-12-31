def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        change = ''
        tmp = ''
        cnt = 1
        for j in range(0, len(s)-i+1, i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                change += str(cnt) + tmp if cnt!=1 else tmp
                tmp = s[j:j+i]
                cnt = 1
            if j == len(s)-i:
                change += str(cnt) + tmp if cnt!=1 else tmp
        if len(s)%i:
            change += str(cnt) + s[len(s)-i-(len(s)%i):] if cnt != 1 else s[len(s)-i-(len(s)%i):]
        
        answer = min(answer, len(change))
        # if change: print(i, change, len(change))
        
            
    return answer