def solution(id_list, report, k):
    answer = []
    dic = {}
    result = {}
    for id in id_list:
        dic[id] = []
        result[id] = 0
        
    for rep in report:
        a, b = rep.split()
        if a not in dic[b]:
            dic[b].append(a)
            
    for id in id_list:
        if len(dic[id]) >= k:
            for res in dic[id]:
                result[res] += 1
    
    for id in id_list:
        answer.append(result[id])
        
    return answer