def jinsu(num, n):
    hihi = []
    while True:
        if num // n == 0:
            if num >= 10:
                num = chr(55+num)
            hihi.append(num)
            break
        tmp = num%n
        if tmp >= 10:
            tmp = chr(55+tmp)
        hihi.append(tmp)
        num = num // n
    hihi.reverse()
    return "".join(map(str,hihi))

def solution(n, t, m, p):   # n : 진법, t : 미리 구할 숫자의 개수, m : 참가 인원, p : 튜브의 순서
    answer = ''
    s = ''
    num = -1
    while len(s) <= t*m:
        num += 1
        s += jinsu(num, n)
        # print(jinsu(num, n))
        # print(s)
    for i in range(p-1, len(s), m):
        answer += s[i]
        if len(answer) == t:
            break
    print(s)
        
    return answer