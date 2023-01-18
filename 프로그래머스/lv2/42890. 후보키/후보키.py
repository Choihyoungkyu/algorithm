from itertools import combinations

def solution(relation):
    answer = 0
    idxs = [i for i in range(len(relation[0]))]
    result_lst = []
    
    # 유일성 구하기
    for i in range(1, len(idxs)+1):
        for combination in combinations(idxs, i):
            tmp_dic = {}  
            for a in relation:
                tmp_str = ""
                for idx in combination:
                    tmp_str += a[idx]
                if tmp_str not in tmp_dic:
                    tmp_dic[tmp_str] = 1
                else:
                    break
            else:
                tmp_str = ""
                for j in combination:
                    tmp_str += str(j)
                result_lst.append(tmp_str)
    
    # 최소성 구하기
    res = []
    for i in result_lst:
        if not res:
            res.append(i)
            answer += 1
            continue
        for j in res:
            for k in j:
                if k not in i:
                    break
            else:
                break
        else:
            res.append(i)
            answer += 1   
    return answer