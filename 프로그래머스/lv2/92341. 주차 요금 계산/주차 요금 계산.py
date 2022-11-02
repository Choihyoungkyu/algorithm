def solution(fees, records):
    def hour(IN, OUT):
        in_H, in_M = map(int, IN.split(':'))
        out_H, out_M = map(int, OUT.split(':'))
        if in_M <= out_M:
            minute = 60*(out_H-in_H) + (out_M-in_M)
        else:
            minute = 60*(out_H-in_H-1) + (60+out_M-in_M)
        return minute
    
    def fee(m):
        if fees[0] >= m:
            tot = fees[1]
        else:
            tot = fees[1] + ((m-fees[0])//fees[2]) * fees[3] 
            if (m-fees[0])%fees[2]:
                tot += fees[3]
        return tot
    
    answer = []
    numbers = {}
    check = {}
    for record in records:
        time, num, state = record.split()
        if state == 'IN':
            check[num] = time
        elif state == 'OUT':
            if num in numbers:
                numbers[num] += hour(check[num], time)
                del(check[num])
            else:
                numbers[num] = hour(check[num], time)
                del(check[num])

    for i in check.keys():
        if i in numbers:
            numbers[i] += hour(check[i], '23:59')
        else:
            numbers[i] = hour(check[i], '23:59')

    lst = []
    for num in numbers:
        lst.append([int(num), fee(numbers[num])])

    lst.sort()
    for i in range(len(lst)):
        answer.append(lst[i][1])
        
    return answer