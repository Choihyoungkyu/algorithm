def solution(routes):
    answer = 0
    routes.sort()
    print(routes)
    end = float('-inf')
    flag = False
    for i in range(len(routes)):
        flag = True
        if end == float('-inf'):
            end = routes[i][1]
            continue
        if end < routes[i][0]:
            answer += 1
            end = routes[i][1]
            flag = False
            if i == len(routes)-1:
                flag = True
        else:
            if end > routes[i][1]:
                end = routes[i][1]
        # print(end)
    if flag:
        answer += 1
    return answer