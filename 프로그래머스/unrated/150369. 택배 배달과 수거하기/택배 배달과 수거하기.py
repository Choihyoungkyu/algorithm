def solution(cap, n, deliveries, pickups):
    answer = 0
    del_idx, pick_idx = n-1, n-1
    while True:
        del_cnt = 0
        pick_cnt = 0
        del_start = del_idx
        pick_start = pick_idx
        del_idx = -1
        pick_idx = -1
        for i in range(del_start, -1, -1):
            if deliveries[i]:
                if del_cnt + deliveries[i] < cap:
                    del_cnt += deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= cap - del_cnt
                    del_cnt = cap
                if del_idx == -1:
                    del_idx = i
                if del_cnt == cap: break
            
        for i in range(pick_start, -1, -1):
            if pickups[i]:
                if pick_cnt + pickups[i] < cap:
                    pick_cnt += pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= cap - pick_cnt
                    pick_cnt = cap
                if pick_idx == -1:
                    pick_idx = i
                if pick_cnt == cap: break
                
        if del_idx == -1 and pick_idx == -1:
            break
        else:
            answer += max(del_idx+1, pick_idx+1) * 2

    return answer