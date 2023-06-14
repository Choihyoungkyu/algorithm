from collections import deque

tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0: break

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float("INF")] * N for _ in range(N)]
    visited[0][0] = arr[0][0]

    answer = 0
    D = ((0, 1), (1, 0), (0, -1), (-1, 0))      # 우하좌상
    que = deque()

    que.append((0, 0))

    while que:
        ci, cj = que.popleft()
        for di, dj in D:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and visited[ci][cj] + arr[ni][nj] < visited[ni][nj]:
                visited[ni][nj] = visited[ci][cj] + arr[ni][nj]
                que.append((ni, nj))

    print(f'Problem {tc}: {visited[N-1][N-1]}')