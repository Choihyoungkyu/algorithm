def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):         # 문자열의 절반까지만 확인하면 됨
        change = ''                         # 단위마다 자른 문자열
        tmp = ''                            # 임시 변수
        cnt = 1                             # 반복 횟수
        for j in range(0, len(s)-i+1, i):   # 단위마다 간격을 둬서 진행
            
            if tmp == s[j:j+i]:             # 뒤의 값이 앞의 값과 같으면
                cnt += 1                    # count 증가
            
            else:                           # 뒤의 값이 앞의 값과 다르면
                change += str(cnt) + tmp if cnt!=1 else tmp # 숫자와 함께 앞의 값을 기록
                tmp = s[j:j+i]              # 임시 변수 재할당
                cnt = 1                     # count 초기화
                
            if j == len(s)-i:               # 단위로 딱 나누어 떨어질 때 마지막 값 처리
                change += str(cnt) + tmp if cnt!=1 else tmp
                
        if len(s)%i:                        # 단위로 안나누어 떨어질 때 마지막 값 처리
            change += str(cnt) + s[len(s)-i-(len(s)%i):] if cnt != 1 else s[len(s)-i-(len(s)%i):]
        
        answer = min(answer, len(change))   # 최소값 갱신
        # if change: print(i, change, len(change))
        
            
    return answer