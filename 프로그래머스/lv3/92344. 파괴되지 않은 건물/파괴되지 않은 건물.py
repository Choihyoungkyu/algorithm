def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    tmp_board = [[0] * m for _ in range(n)]
    for type, r1, c1, r2, c2, degree in skill:
        # for i in tmp_board:
        #     print(i)
        # print()
        tmp_board[r1][c1] += degree if type==2 else -degree
        if c2+1 < m:
            tmp_board[r1][c2+1] += -degree if type==2 else degree
        if r2+1 < n:
            tmp_board[r2+1][c1] += -degree if type==2 else degree
        if r2+1 < n and c2+1 < m:
            tmp_board[r2+1][c2+1] += degree if type==2 else -degree

    # for i in tmp_board:
    #     print(i)
    # print()
            
    for i in range(n):
        for j in range(1, m):
            tmp_board[i][j] += tmp_board[i][j-1]
            
    # for i in tmp_board:
    #     print(i)
    # print()
            
    for j in range(m):
        for i in range(1, n):
            tmp_board[i][j] += tmp_board[i-1][j]
            
    # for i in tmp_board:
    #     print(i)
    # print()
            
    for i in range(n):
        for j in range(m):
            answer += 1 if board[i][j] + tmp_board[i][j] > 0 else 0
            # tmp_board[i][j] += board[i][j]
    
    # for i in tmp_board:
    #     print(i)
    # print()
            
    return answer