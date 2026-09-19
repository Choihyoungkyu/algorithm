import copy

def rotate(n, m, arr, query):
    min_v = 999999
    tmp = copy.deepcopy(arr)
    si, sj, ei, ej = query[0]-1, query[1]-1, query[2]-1, query[3]-1
    D = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 시계방향
    ci, cj = si, sj
    while True:
        for di, dj in D:
            ni, nj = ci+di, cj+dj
            if si <= ni <= ei and sj <= nj <= ej and (si == ni or ei == ni or sj == nj or ej == nj) and arr[ni][nj] == tmp[ni][nj]:
                arr[ni][nj] = tmp[ci][cj]
                min_v = min(min_v, arr[ni][nj])
                ci, cj = ni, nj
                break
        else:
            break
    return min_v

def solution(rows, columns, queries):
    answer = []
    n, m = rows, columns
    num = 0
    arr = [[0 for _ in range(m)] for _ in range(n)]
    # 배열 만들기
    for i in range(n):
        for j in range(m):
            num += 1
            arr[i][j] = num
            
    for query in queries:
        answer.append(rotate(n, m, arr, query))
        # for i in range(n):
        #     print(arr[i], answer)
    return answer