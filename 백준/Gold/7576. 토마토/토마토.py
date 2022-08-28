import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

def DFS(lst):
    global cnt
    visited = deque([0] * M for _ in range(N))
    # visited = [[0] * M for _ in range(N)]
    D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    lst2 = deque()
    num = 0
    queue = deque()
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                queue.append([i, j])
                visited[i][j] = 1
            elif lst[i][j] == 0:
                num += 1
            else:
                visited[i][j] = -1
    if num == 0 and len(lst2) != 0:
        return 0

    tmp = deque()
    while queue:
        ni, nj = queue.popleft()
        for di, dj in D:
            if 0<=ni+di<N and 0<=nj+dj<M and lst[ni+di][nj+dj]==0 and visited[ni+di][nj+dj] == 0:
                tmp.append([ni+di, nj+dj])
                visited[ni+di][nj+dj] = cnt
                num -= 1
            
        if queue == deque() and tmp != deque():
            queue = tmp
            cnt += 1
            tmp = deque()

    if num != 0:
        return -1
    else:
        return cnt-1


M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cnt = 1
print(DFS(lst))
