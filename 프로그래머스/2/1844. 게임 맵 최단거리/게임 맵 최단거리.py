def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    D = ((0, 1), (0, -1), (1, 0), (-1, 0))
    # for map in maps:
    #     print(map)
    que = [[0, 0]]
    while len(que) > 0:
        ci, cj = que.pop(0)
        for di, dj in D:
            ni, nj = ci+di, cj+dj
            if ni == n-1 and nj == m-1: return visited[ci][cj] + 1
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0 and maps[ni][nj] == 1:
                visited[ni][nj] = visited[ci][cj] + 1
                que.append([ni, nj])
        # for i in range(n):
        #     print(visited[i])
        # print()
    return -1