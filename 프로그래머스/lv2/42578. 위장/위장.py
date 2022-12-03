# from itertools import combinations 

def solution(clothes):
    answer = 1
    dic = {}
    for cloth, kind in clothes:
        if kind not in dic:
            dic[kind] = []
        dic[kind].append(cloth)
    cnt_lst = [0] * len(dic)
    i = 0
    for key in dic.keys():
        cnt_lst[i] =len(dic[key])
        i += 1
    
    for num in cnt_lst:
        answer *= (num+1)
    
    # for i in range(1, len(cnt_lst)+1):
    #     for j in combinations(cnt_lst, i):
    #         tmp = 0
    #         for k in j:
    #             if not tmp:
    #                 tmp = k
    #             else:
    #                 tmp *= k
    #         answer += tmp
        
    # def comb(n):
    #     lst = []
    #     tot = 0
    #     for i in range(0, 1<<n):
    #         tmp = []
    #         for j in range(0, n):
    #             if i & (1<<j):
    #                 tmp.append(cnt_lst[j])
    #         lst.append(tmp[:])
    #     for i in lst:
    #         tmp = 0
    #         for num in i:
    #             if not tmp:
    #                 tmp = num
    #             else:
    #                 tmp *= num
    #         tot += tmp
    #     return tot
    # answer = comb(len(cnt_lst))
    
    return answer-1