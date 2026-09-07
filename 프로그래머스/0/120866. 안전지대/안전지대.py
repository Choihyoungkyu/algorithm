def solution(board):
    l = len(board)
    answer = l*l
    visited = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            if board[i][j] == 1:
                answer -= bomb(l, i, j, visited, board) + 1
    return answer

def bomb(l, i, j, visited, board):
    D = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
    cnt = 0
    for di, dj in D:
        ni, nj = i+di, j+dj
        if 0<=ni<l and 0<=nj<l and visited[ni][nj] != 1 and board[ni][nj] != 1:
            visited[ni][nj] = 1
            cnt += 1
    return cnt