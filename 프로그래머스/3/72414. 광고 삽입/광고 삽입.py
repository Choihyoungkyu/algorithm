def solution(play_time, adv_time, logs):
    answer = ''
    play_length = time_to_second(play_time)+1
    adv_length = time_to_second(adv_time)
    DP = [0] * play_length
    
    # 이거 예전에 터렛 문제였나 풀었던 방식
    for log in logs:
        start, end = log.split("-")
        DP[time_to_second(start)] += 1
        DP[time_to_second(end)] -= 1
        
    for i in range(1, play_length):
        DP[i] = DP[i-1] + DP[i]
    
    answer = sliding_window(DP, play_length, adv_length)
    
    return answer

def sliding_window(DP, play_length, adv_length):
    # 처음 윈도우 내 총합 구하기
    watching_time = 0
    for i in range(adv_length):
        watching_time += DP[i]
        
    max_time = watching_time
    max_idx = 0
    # 윈도우 움직이면서 총합 바꾸기
    for i in range(1, play_length - adv_length):
        watching_time += DP[i+adv_length] - DP[i]
        if max_time < watching_time:    # 시간이 같은 경우 빠른걸 뽑으면 되니까 <= 대신 < 사용
            max_time = watching_time
            max_idx = i+1
            # ex) [0, 0, 1, 1, 1, 1, ...] -> i == 1인 경우 window가 2부터 시작이므로 +1 해줘야 됨!
            
    return second_to_time(max_idx)

def time_to_second(time):
    return int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:])

def second_to_time(second):
    s = ""
    if second // 3600 < 10:
        s += f'0{second // 3600}:'
    else:
        s += f'{second // 3600}:'
    second %= 3600
    if second // 60 < 10:
        s += f'0{second // 60}:'
    else:
        s += f'{second // 60}:'
    second %= 60
    if second < 10:
        s += f'0{second}'
    else:
        s += f'{second}'
    return s