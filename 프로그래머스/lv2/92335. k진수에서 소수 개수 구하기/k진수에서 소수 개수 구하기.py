def solution(n, k):
    answer = -1
    if k != 10:
        change_num = ''
        while n:
            change_num += str(n%k)
            n //= k
        s = ''
        for i in change_num:
            s = i + s
    else:
        s = str(n)
    
    # print(f's : {s}')
    
    def f(s):
        num = int(s)
        for i in range(2, int(num**0.5)+1):    # 2인 경우도 포함시키기 위해 +2를 해줌
            if num % i == 0:
                break
        else:
            return 1
        return 0
    
    tmp = ''
    cnt = 0
    check = []
    for i in range(len(s)):
        if 0 < int(s[i]) < 10:
            tmp += s[i]
        else:
            if tmp and tmp != '1':
                if tmp in check:
                    cnt += 1
                elif f(tmp):
                    cnt += 1
                    check.append(tmp)
                # print(f'count : {tmp}')
            tmp = ''
    
    if tmp and tmp != '1':
        if tmp in check or f(tmp):
            cnt += 1
        # print(f'count : {tmp}')
            
    answer = cnt
    return answer