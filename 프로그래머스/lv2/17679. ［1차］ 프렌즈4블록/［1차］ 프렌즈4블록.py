# block인 부분 폭파시키기
def is_block(m, n, i, j, board, visited):
    tmp = 0
    if i+1 < m and j+1 < n:
        if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
            if not visited[i][j]:
                visited[i][j] = 1
                tmp += 1
            if not visited[i+1][j]:
                visited[i+1][j] = 1
                tmp += 1
            if not visited[i][j+1]:
                visited[i][j+1] = 1
                tmp += 1
            if not visited[i+1][j+1]:
                visited[i+1][j+1] = 1
                tmp += 1
    return tmp

# 폭파시킨 후 요소들 내리기 --> 쭉 내려야됨
def down(m, n, board):
    for j in range(n):
        for i in range(m-1, -1, -1):
            if board[i][j] == 0:
                k = 0
                while 0<i-k:
                    k += 1
                    if board[i-k][j]:
                        board[i][j] = board[i-k][j]
                        board[i-k][j] = 0
                        break
            
def solution(m, n, board):
    answer = 0
    block = []
    board = [list(s) for s in board]
    while True:
        visited = [[0] * n for _ in range(m)]
        check = answer
        for i in range(m):
            for j in range(n):
                if board[i][j]:
                    num = is_block(m, n, i, j, board, visited)
                    answer += num
        #             if num:
        #                 down(m, n, board)
        # if check == answer:
        #     break
        if check == answer:
            break
        else:
            for i in range(m):
                for j in range(n):
                    if visited[i][j]:
                        board[i][j] = 0
            down(m, n, board)

    return answer