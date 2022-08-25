import sys
input = lambda: sys.stdin.readline().strip()

def DFS(lst):
    global cnt
    visited = [[0] * M for _ in range(N)]
    D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                queue = []
                queue.append([i, j])
                visited[i][j] = 1
                lst[i][j] = 0
                cnt += 1
                while queue:
                    ni, nj = queue.pop(0)
                    for di, dj in D:
                        if 0<=ni+di<N and 0<=nj+dj<M and lst[ni+di][nj+dj]==1 and visited[ni+di][nj+dj] != 1:
                            queue.append([ni+di, nj+dj])
                            visited[ni+di][nj+dj] = 1
                            lst[ni+di][nj+dj] = 0

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    lst = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        lst[y][x] = 1
    cnt = 0
    DFS(lst)
    print(cnt)