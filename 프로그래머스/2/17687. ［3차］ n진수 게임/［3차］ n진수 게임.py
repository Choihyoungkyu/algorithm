def change(num):
    if num >= 10:
        return chr(55 + num)
    else:
        return str(num)

def solution(n, t, m, p):   # n : 진법, t : 미리 구할 숫자의 개수, m : 참가 인원, p : 튜브의 순서
    answer = ''
    arr = ['0']
    num = 1
    
    while len(arr) < t * m:
        mok = num
        tmp = []
        while mok > 0:
            if mok // n == 0:
                tmp.append(change(mok))
                break
            tmp.append(change(mok % n))
            mok = mok // n
        tmp.reverse()
        arr += tmp
        num += 1
        
    for i in range(t * m):
        if (i+1) % m == p % m:
            answer += arr[i]
    
    return answer