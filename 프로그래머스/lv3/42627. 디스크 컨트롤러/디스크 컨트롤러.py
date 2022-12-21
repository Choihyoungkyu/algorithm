def solution(jobs):
    jobs.sort()
    answer = 0
    length = len(jobs)
    
    current_time = jobs[0][0]+jobs[0][1]
    tot_time = jobs[0][1]
    jobs.pop(0)
    while jobs:
        print(tot_time)
        print(current_time)
        waiting = []
        for idx in range(len(jobs)):
            if jobs[idx][0] <= current_time:
                waiting.append([jobs[idx][1], idx])
            else:
                break
        if not waiting:
            print(f'1 - {jobs[0]}')
            current_time += (jobs[0][0]-current_time)+jobs[0][1]
            tot_time += jobs[0][1]
            jobs.pop(0)
        else:
            waiting.sort()
            idx = waiting[0][1]
            print(f'2 - {jobs[idx]}')
            current_time += jobs[idx][1]
            tot_time += current_time-jobs[idx][0]
            jobs.pop(idx)
    
    print(tot_time)
    print(current_time)
        
    answer = tot_time//length
    return answer
