import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(i, j):
    if arr[i][j] != 0: return
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    while queue:
        ci, cj = queue.popleft()
        arr[ci][cj] = -1
        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = 1

cnt = 0
for i in range(N):
    bfs(i, 0)
    bfs(i, M-1)
for j in range(1, M-1):
    bfs(0, j)
    bfs(N-1, j)


while True:
    cnt += 1
    lst = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                tmp = 0
                for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == -1:
                        tmp += 1
                        if tmp == 2:
                            arr[i][j] = 0
                            lst.append((i, j))
                            break

    if len(lst) == 0:

        print(cnt-1)
        break
    else:
        for i, j in lst:
            bfs(i, j)

