def solution(gems):
    answer = []
    gems_set = list(set(gems))
    start = 0
    end = -1
    tmp = {}
    while True:
        if len(tmp) != len(gems_set):
            end += 1
            if end < len(gems):
                if gems[end] not in tmp:
                    tmp[gems[end]] = 0
                tmp[gems[end]] += 1
                
            
        elif len(tmp) == len(gems_set):
            answer.append([abs(end-start), start+1, end+1])
            tmp[gems[start]] -= 1
            if tmp[gems[start]] == 0:
                del tmp[gems[start]]
            start += 1
        if start == len(gems) or end == len(gems):
            break
        # print(tmp)
    answer.sort()
    # print(answer)
    return answer[0][1:]