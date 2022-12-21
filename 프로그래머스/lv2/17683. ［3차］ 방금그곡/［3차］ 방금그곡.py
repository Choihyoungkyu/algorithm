def solution(m, musicinfos):
    # musicinfos : "시작한 시각, 끝난 시각, 음악 제목, 악보 정보"
    answer = '(None)'
    musicinfo_list = []
    for i in musicinfos:
        lst = list(i.split(","))
        musicinfo_list.append(lst)
    
    def getTime(st, et):
        st_h, st_m = map(int, st.split(":"))
        et_h, et_m = map(int, et.split(":"))
        minute = (et_h-st_h) * 60
        if et_h - st_h >= 0:
            minute += et_m - st_m
        else:
            minute -= et_m - st_m
        return minute

    def changeStr(s):
        result = ""
        i = 1
        while i < len(s):
            if s[i] == "#":
                result += s[i-1].lower()
                i += 2
            else:
                result += s[i-1]
                i += 1
        if s[-1] != "#":
            result += s[-1]
        return result
    
    m = changeStr(m)
    result = []
    for info in musicinfo_list:
        title = changeStr(info[2])
        song = changeStr(info[3])
        time = getTime(info[0], info[1])
        print(time, m, title, song)
        if len(song) > time:
            if time - len(m) < 0:
                continue
            for i in range(time-len(m)+1):
                for j in range(len(m)):
                    if song[(i+j)%len(song)] != m[j]:
                        break
                else:
                    if not result:
                        result = [title, time]
                    elif result[1] < time:
                        result = [title, time]
                    break
        else:
            if time+(len(song)-(time%len(song)))-len(m) < 0:
                continue
            for i in range(time+(len(song)-(time%len(song)))-len(m)+1):
                for j in range(len(m)):
                    if song[(i+j)%len(song)] != m[j]:
                        break
                else:
                    if not result:
                        result = [title, time]
                    elif result[1] < time:
                        result = [title, time]
                    break

    if result:
        answer = result[0]
    return answer