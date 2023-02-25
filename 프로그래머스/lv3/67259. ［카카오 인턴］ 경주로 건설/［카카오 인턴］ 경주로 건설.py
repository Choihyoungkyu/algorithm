def dfs(i, j, board, answer, D):
    visited = [[float('INF')] * len(board) for _ in range(len(board))]
    visited[i][j] = 0
    check = [[[] for _ in range(len(board))] for _ in range(len(board))]
    dir = (0, 0)
    stack = []
    while True:
        for di, dj in D:
            ni, nj = i+di, j+dj
            if 0<=ni<len(board) and 0<=nj<len(board) and board[ni][nj] != 1:
                if dir == (0, 0) and visited[ni][nj] > visited[i][j] + 100:
                    visited[ni][nj] = visited[i][j] + 100
                    stack.append((i, j, dir))
                    dir = (di, dj)
                    check[ni][nj] = [dir]
                    i, j = ni, nj
                    break
                elif dir == (di, dj) and visited[ni][nj] > visited[i][j] + 100:
                    visited[ni][nj] = visited[i][j] + 100
                    stack.append((i, j, dir))
                    check[ni][nj] = [dir]
                    i, j = ni, nj
                    break
                elif dir != (di, dj) and visited[ni][nj] > visited[i][j] + 600:
                    visited[ni][nj] = visited[i][j] + 600
                    stack.append((i, j, dir))
                    dir = (di, dj)
                    check[ni][nj] = [dir]
                    i, j = ni, nj
                    break
                elif dir != (di, dj) and visited[ni][nj] == visited[i][j] + 600 and (di, dj) not in check[ni][nj]:
                    stack.append((i, j, dir))
                    dir = (di, dj)
                    check[ni][nj].append(dir)
                    i, j = ni, nj
                    break
                elif dir == (di, dj) and visited[ni][nj] == visited[i][j] + 100 and (di, dj) not in check[ni][nj]:
                    stack.append((i, j, dir))
                    dir = (di, dj)
                    check[ni][nj].append(dir)
                    i, j = ni, nj
                    break
        else:
            if stack:
                i, j, dir = stack.pop()
            else:
                # for k in check:
                #     print(*k)
                answer.append(visited[-1][-1])
                return

def solution(board):
    answer = []
    dfs(0, 0, board, answer, ((0, 1), (1, 0), (-1, 0), (0, -1)))
    dfs(0, 0, board, answer, ((1, 0), (0, 1), (-1, 0), (0, -1)))
    # for i in arr:
    #     print(*i)
    return min(answer)