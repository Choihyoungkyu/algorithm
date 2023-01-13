from collections import defaultdict

def binary_search(lst, tar):
    s = 0
    e = len(lst) - 1
    while s <= e:
        mid = (s+e) // 2
        if lst[mid] < tar:
            s = mid+1
        else:
            e = mid-1
    return s

def solution(info, query):
    # 언어, 직군, 경력, 소울푸드, 점수
    lst = [("-", "cpp", "java", "python"),
          ("-", "backend", "frontend"),
          ("-", "junior", "senior"),
          ("-", "chicken", "pizza")]
    answer = []
    
    # info, query 리스트화
    infos = [list(i.split()) for i in info]
    querys = []
    for q in query:
        tmp_lst = []
        for i in q.split():
            if i == "and":
                continue
            tmp_lst.append(i)
        querys.append(tmp_lst)
    
    # 각 조건별로 분류해놓기
    dic = defaultdict(list)
    for i in lst[0]:
        for j in lst[1]:
            for k in lst[2]:
                for m in lst[3]:
                    for info in infos:
                        if (i == "-" or i == info[0]) and (j == "-" or j == info[1]) and (k == "-" or k == info[2]) and (m == "-" or m == info[3]):
                            dic[i+j+k+m].append(int(info[4]))
    
    # dic 정렬
    for key in dic.keys():
        dic[key].sort()
    # print(dic)
    # query별 만족 인스턴스 개수 구하기
    for query in querys:
        cnt = 0
        s = "".join(query[:4])
            
        # ** 이진탐색으로 개수 찾는 방법 적용하기 **
        idx = binary_search(dic[s], int(query[4]))
        
        answer.append(len(dic[s])-idx)
    return answer