def solution(gems):
    answer = []
    gems_set = list(set(gems))
    start = 0
    end = -1
    tmp = {}
    
    while True:
        # 조건 만족 X => 끝점 이동
        if len(tmp) != len(gems_set):
            end += 1
            if end < len(gems):
                if gems[end] not in tmp:
                    tmp[gems[end]] = 0
                tmp[gems[end]] += 1
                
        # 조건 만족 O => 시작점 이동
        elif len(tmp) == len(gems_set):
            answer.append([end-start, start+1, end+1])
            tmp[gems[start]] -= 1
            if tmp[gems[start]] == 0:
                del tmp[gems[start]]
            start += 1
            
        # 종료 조건
        if start == len(gems) or end == len(gems):
            break
            
    answer.sort()
    return answer[0][1:]