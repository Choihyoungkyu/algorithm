def solution(n, info):
    global maxV, maxS, idx
    answer = []
    maxV = 0
    maxS = []
    idx = 0

    # 가장 낮은 점수를 더 많이 맞힌 경우 구현하기
    # maxV < tot랑 maxV == tot 나눠서 구현하기
    
    def f(i, tot, s, cnt):
        global maxV, maxS, idx
        if i == 11:
            if maxV < tot:
                maxV = tot
                s = list(map(int, s.strip().split()))
                maxS = s[:]
                for j in range(len(maxS)-1, -1, -1):
                    if s[j]:
                        idx = j
                        print(idx)
                        break
            elif maxV == tot:
                s = list(map(int, s.strip().split()))
                if maxS:
                    for j in range(len(maxS)-1, idx-1, -1):
                        if s[j] > maxS[j]:
                            maxS = s[:]
                            break
                return
        else:
            if cnt and cnt > info[i] :
                f(i+1, tot+(10-i), s+str(info[i]+1)+' ', cnt-(info[i]+1))
            if info[i]:
                f(i+1, tot-(10-i), s+'0 ', cnt)
            else:
                f(i+1, tot, s+'0 ', cnt)

    f(0, 0, '', n)
    answer = maxS
    
    if not answer or maxV == 0:
        answer = [-1]
    else:
        cnt = 0
        for i in range(11):
            cnt += answer[i]
        if n-cnt:
            answer[10] += n-cnt
    return answer
