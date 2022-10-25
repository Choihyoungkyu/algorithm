import sys
input = lambda:sys.stdin.readline().strip()

D = [[-1, 0], [0, -1], [1, 0], [0, 1]]     # 북서남동

N, M = map(int, input().split())
# r : 북쪽으로부터 떨어진 칸의 개수, c : 서쪽으로부터 떨어진 칸의 개수
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
stack = []
cnt = 1
if d == 1:
    d = 3
elif d == 3:
    d = 1
def dfs(i, j, d):
    global cnt
    visited[i][j] = 1
    while True:
        for k in range(1, 5):
            ni, nj = i+D[(d+k)%4][0], j+D[(d+k)%4][1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                flag = False
                visited[ni][nj] = 1
                cnt += 1
                i, j, d = ni, nj, (d+k)%4
                break
        else:
            ni, nj = i-D[d][0], j-D[d][1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                i, j = ni, nj
            else:
                return cnt
dfs(r, c, d)
print(cnt)
