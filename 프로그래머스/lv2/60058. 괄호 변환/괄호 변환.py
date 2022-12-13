def solution(p):
    answer = ''
    
    def validStr(w):            # 올바른 괄호 문자열인지 확인
        cnt = 0
        for st in w:
            if st == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                return False
        return True    
    
    def split(w):              # u와 v로 나누기
        u = ""
        v = ""
        if not w:
            return
        check_str = ""
        cnt = 1
        for st in w:
            if cnt == 0:
                v += st
                continue
            if not check_str:
                check_str = st
                u += st
                continue
            if st == check_str:
                cnt += 1
            else:
                cnt -= 1
            u += st
        return u, v
    
    def f(v):                   # 문제에 나온 알고리즘
        tmp = ""
        u, v = split(v)
        if validStr(u):
            tmp += u
            if v:
                tmp += f(v)
        else:
            tmp += "("
            if v:
                tmp += f(v)
            tmp += ")"
            for i in range(1, len(u)-1):
                if u[i] == "(":
                    tmp += ")"
                else:
                    tmp += "("
        return tmp
    answer = f(p)
    return answer