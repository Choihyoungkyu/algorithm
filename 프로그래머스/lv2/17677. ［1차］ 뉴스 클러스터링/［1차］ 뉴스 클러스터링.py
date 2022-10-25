def solution(str1, str2):
    answer = 0
    tmp1 = []
    for i in range(len(str1)-1):
        s = str1[i] + str1[i+1]
        if s.isalpha():
            tmp1.append(s.lower())
    tmp2 = []
    for i in range(len(str2)-1):
        s = str2[i] + str2[i+1]
        if s.isalpha():
            tmp2.append(s.lower())
    A = 0
    B = 0
    check = []
    for i in range(len(tmp1)):
        if (tmp1[i] in tmp2) and (tmp1[i] not in check):
            A += min(tmp1.count(tmp1[i]), tmp2.count(tmp1[i]))
            B += max(tmp1.count(tmp1[i]), tmp2.count(tmp1[i]))
            check.append(tmp1[i])
        elif (tmp1[i] not in tmp2) and (tmp1[i] not in check):
            B += tmp1.count(tmp1[i])
            check.append(tmp1[i])
    for j in range(len(tmp2)):
        if tmp2[j] not in check:
            B += tmp2.count(tmp2[j])
            check.append(tmp2[j])
    # print(A, B)
    if A or B:
        answer = int(65536 * (A / B))
    else:
        answer = 65536
    return answer