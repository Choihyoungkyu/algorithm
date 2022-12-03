from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    dic = defaultdict(int)
    for order in orders:
        for i in range(len(course)):
            for j in combinations(order, course[i]):
                j = list(j)
                j.sort()
                tmp = "".join(j)
                dic[tmp] += 1
                
    tmp = [[] for _ in range(len(course))]
    for pick, num in dic.items():
        if num >= 2:
            if tmp[course.index(len(pick))]:
                if num == tmp[course.index(len(pick))][0][1]:
                    tmp[course.index(len(pick))].append([pick, num])
                elif num > tmp[course.index(len(pick))][0][1]:
                    tmp[course.index(len(pick))] = [[pick, num]]
                else:
                    pass
            else:
                tmp[course.index(len(pick))] = [[pick, num]]

    for i in tmp:
        for j in i:
            answer.append(j[0])
    answer.sort()
    return answer