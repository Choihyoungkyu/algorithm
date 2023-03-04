def solution(n, k, cmd):
    answer = ''
    array = [[False, idx-1, idx+1] for idx in range(n)] # 삭제 유무, 위쪽, 아래쪽
    idx = k
    stack = []
    for command in cmd:
        lst = list(command.split(' '))
        # print(lst)
        if len(lst) > 1:
            if lst[0] == "U":
                for _ in range(int(lst[1])):
                    idx = array[idx][1]
            else:
                for _ in range(int(lst[1])):
                    idx = array[idx][2]
        else:
            if lst[0] == "C":
                stack.append(idx)
                array[idx][0] = True
                if array[idx][1] >= 0:
                    array[array[idx][1]][2] = array[idx][2]
                if array[idx][2] <= n-1:
                    array[array[idx][2]][1] = array[idx][1]
                if array[idx][2] <= n-1:
                    idx = array[idx][2]
                else:
                    idx = array[idx][1]
            else:
                tmp_idx = stack.pop()
                array[tmp_idx][0] = False
                if array[tmp_idx][1] >= 0:
                    array[array[tmp_idx][1]][2] = tmp_idx
                if array[tmp_idx][2] <= n-1:
                    array[array[tmp_idx][2]][1] = tmp_idx
        # print(array)
    for i in range(n):
        answer += 'X' if array[i][0] else 'O'
    return answer