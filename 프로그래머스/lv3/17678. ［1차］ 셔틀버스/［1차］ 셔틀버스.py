def formatting(hour, minute):
    if 0 < int(minute) <= 10:
        if 0 < int(hour) < 10:
            return "0"+str(int(hour))+":0"+str(int(minute)-1)
        else:
            return hour+":0"+str(int(minute)-1)
    elif int(minute) == 0:
        if 0 < int(hour) <= 10:
            return "0"+str(int(hour)-1)+":59"
        else:
            return str(int(hour)-1)+":59"
    else:
        return hour+":"+str(int(minute)-1)

def solution(n, t, m, timetable):
    cnt_n = 1                           # 버스 지나간 수
    cnt_m = 0                           # 현재 버스 인원 수 체크
    end_time = 540+t*(n-1)              # 막차 시간
    
    timetable.sort()
    i = 0
    
    while i < len(timetable):
        hour, minute = timetable[i].split(":")
        minutes = int(hour)*60 + int(minute)    # 승객의 탑승 시간
        current_bus = 540+t*(cnt_n-1)           # 현재 버스 시간
        
        # 탑승 가능한 경우
        if current_bus >= minutes:
            
            # 남은 버스가 없고 인원수 다 찰 경우
            if cnt_m + 1 == m and cnt_n == n:                
                return formatting(hour, minute)
            
            # 막차를 타야만하는 경우1 : 남은 크루가 있지만 막차 시간보다 늦게 올 경우
            if minutes > end_time:
                return formatting(str(end_time//60), str(end_time%60+1))
            
            i += 1
            cnt_m += 1
            if cnt_m == m:
                cnt_m = 0
                cnt_n += 1
        
        # 해당 버스시간을 놓친 경우
        else:
            cnt_n += 1          # 다음 버스 ㄱ
            cnt_m = 0
        
        # 막차를 타야만하는 경우2 : 마지막 버스가 다 찰 경우
        if cnt_n > n:
            return formatting(str(end_time//60), str(end_time%60+1))
    
    # 막차를 타야만하는 경우3 : 모든 크루들이 다 탔을 경우
    return formatting(str(end_time//60), str(end_time%60+1))