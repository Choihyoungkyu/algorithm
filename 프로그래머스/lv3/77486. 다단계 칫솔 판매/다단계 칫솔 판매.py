def sell(tot):
    bbing = int(tot * 0.1)
    return (tot-bbing, bbing)

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    dic = {}
    for i in range(len(enroll)):
        dic[enroll[i]] = i
    for i in range(len(seller)):
        idx = dic[seller[i]]                    # 판매원이 누구냐
        me = enroll[idx]                        # 나다
        tot = amount[i] * 100                   # 판매액
        
        while True:
            yangachi = referral[idx]            # 나를 다단계로 꼬신놈
            my_money, bbing = sell(tot)         # 돈 계산
            answer[idx] += my_money             # 내 돈 챙기자
            tot = bbing                         # 삥 뜯긴걸로 갱신
            if yangachi == "-" or tot < 1: break    # 종료 조건
            idx = dic[yangachi]                 # 다음 희생자 계산
            me = enroll[idx]                    # 이제 내가 희상자다
            
    return answer