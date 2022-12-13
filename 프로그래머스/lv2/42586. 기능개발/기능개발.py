def solution(progresses, speeds):
    answer = []
    
    current = 0
    days = 0
    
    while True:
        cnt = 1
        days += (100 - (progresses[current] + speeds[current]*days)) // speeds[current] + 1
        if (100 - (progresses[current] + speeds[current]*days)) % speeds[current] == 0:
            days -= 1
        for idx in range(current+1, len(progresses)):
            current = idx
            if progresses[idx] + speeds[idx]*days >= 100:
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 0
                break
        if current == len(progresses)-1 and cnt:
            answer.append(cnt)
            break
    
    return answer