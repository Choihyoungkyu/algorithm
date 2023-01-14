def solution(triangle):
    answer = 0
    answer_lst = [triangle[0]]
    # [7], [10, 15], [18, 16, 15], ...
    for i in range(1, len(triangle)):
        tmp = [0] * (i+1)
        for j in range(len(triangle[i-1])):
            tmp[j] = max(tmp[j], answer_lst[i-1][j]+triangle[i][j])
            tmp[j+1] = max(tmp[j+1], answer_lst[i-1][j]+triangle[i][j+1])
        answer_lst.append(tmp)
    # print(answer_lst)
    answer = max(answer_lst[-1])
    return answer