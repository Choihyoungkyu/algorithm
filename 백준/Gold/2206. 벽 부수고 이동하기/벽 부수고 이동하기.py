import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
D = [[0, 1], [1, 0], [0, -1], [-1, 0]]

visited = [[0]*M for _ in range(N)]
visited2 = [[0]*M for _ in range(N)]
visited[0][0] = 1
ans = -1

que = deque()
que.append([0, 0, 0])
while que:
    ci, cj, flag = que.popleft()
    for di, dj in D:
        ni, nj = ci+di, cj+dj
        if flag:
            if 0<=ni<N and 0<=nj<M and (visited2[ni][nj]==0 or visited2[ni][nj]>visited2[ci][cj]+1) and arr[ni][nj]=='0':
                que.append([ni, nj, flag])
                visited2[ni][nj] = visited2[ci][cj]+1
        else:
            if 0<=ni<N and 0<=nj<M and (visited[ni][nj]==0 or visited[ni][nj]>visited[ci][cj]+1):
                if arr[ni][nj] == '1':
                    que.append([ni, nj, flag+1])
                    visited2[ni][nj] = visited[ci][cj]+1
                else:
                    que.append([ni, nj, flag])
                    visited[ni][nj] = visited[ci][cj]+1

    if visited[N-1][M-1]:
        ans = visited[N-1][M-1]
        break
    if visited2[N-1][M-1]:
        ans = visited2[N-1][M-1]
        break

# for i in arr:
#     print(i)
# print()
# for i in visited:
#     print(i)
# print()
# for i in visited2:
#     print(i)
# print()
print(ans)