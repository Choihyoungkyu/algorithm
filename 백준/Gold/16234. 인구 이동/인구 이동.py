from collections import deque

N, L, R = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    val = list(map(int, input().split()))
    for j in range(N):
        arr[i][j] = val[j]

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = -1
    sumV = arr[i][j]
    cnt = 1
    D = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while queue:
        ci, cj = queue.popleft()
        for di, dj in D:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and L <= abs(arr[ci][cj] - arr[ni][nj]) <= R and visited[ni][nj] == 0:
                sumV += arr[ni][nj]
                queue.append((ni, nj))
                visited[ni][nj] = -1
                cnt += 1

    if cnt == 1:
        return False
    
    for ii in range(N):
        for jj in range(N):
            if visited[ii][jj] == -1:
                visited[ii][jj] = sumV // cnt

    return True

answer = 0

while True:
    flag = False
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                if BFS(i, j):
                    flag = True
                else:
                    visited[i][j] = arr[i][j]
    if not flag:
        break
    answer += 1
    for i in range(N):
        arr[i] = visited[i]

print(answer)