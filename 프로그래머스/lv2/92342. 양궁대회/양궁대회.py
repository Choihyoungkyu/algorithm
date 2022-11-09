def solution(n, info):
    global maxV, maxS, idx
    answer = []
    maxV = 0                        # 가장 큰 점수 차이
    maxS = []                       # 라이언 과녁 정보
    idx = 0                         # 가장 작은 점수를 맞힌 위치
    
    def f(i, tot, s, cnt):
        global maxV, maxS, idx
        if i == 11:                 # 과녁에 활을 다 쏜 경우
            if maxV < tot:          # 점수차를 갱신해야 할 경우
                maxV = tot          # 점수차 갱신
                s = list(map(int, s.strip().split()))   # 최대 점수차의 과녁 정보를 저장
                maxS = s[:]
                for j in range(len(maxS)-1, -1, -1):    # 해당 과녁의 가장 작은 점수의 위치를 저장
                    if s[j]:
                        idx = j
                        break
            elif maxV == tot:                           # 점수차가 최대 점수차와 같은 경우
                s = list(map(int, s.strip().split()))
                if maxS:
                    for j in range(len(maxS)-1, idx-1, -1): # 가장 작은 점수의 위치 비교 및 개수 비교 후 과녁 정보 저장
                        if s[j] > maxS[j]:
                            maxS = s[:]
                            break
                return
            
        else:                                           # 과녁에 활을 쏘는 경우
            if cnt and cnt > info[i] :                  # 라이언이 이기는 경우 : 어피치보다 +1개를 더 맞혀야 됨
                f(i+1, tot+(10-i), s+str(info[i]+1)+' ', cnt-(info[i]+1))
            if info[i]:                                 # 어피치가 이기는 경우 : 화살 안씀
                f(i+1, tot-(10-i), s+'0 ', cnt)
            else:                                       # 둘 다 0인 경우
                f(i+1, tot, s+'0 ', cnt)

    f(0, 0, '', n)
    answer = maxS
    
    if maxV == 0:                         # 라이언이 이길 수 없는 경우 : maxV == 0 인 경우
        answer = [-1]
    else:                                               # 라이언이 이기는데 화살을 다 안쓰고 이기면 마지막 0점에 몰아주기
        cnt = 0
        for i in range(11):
            cnt += answer[i]
        if n-cnt:
            answer[10] += n-cnt
    return answer
