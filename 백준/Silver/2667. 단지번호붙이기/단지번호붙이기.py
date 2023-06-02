import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
lst = [list(map(int,input())) for _ in range(N)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 우좌하상

def dfs(ni, nj, res):
    stack = [0] * (N * N)
    top = -1
    cnt = 1
    lst[ni][nj] = 0
    while True:
        for di, dj in d:
            if 0<=ni+di<N and 0<=nj+dj<N and lst[ni+di][nj+dj] == 1:
                top += 1
                cnt += 1
                stack[top] = [ni, nj]
                ni += di
                nj += dj
                lst[ni][nj] = 0
                break
        else:
            if top != -1:
                ni, nj = stack[top]
                top -= 1
            else:
                res.append(cnt)
                break
    return res

res = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            ni = i
            nj = j
            dfs(ni, nj, res)
res.sort()
print(len(res))
for i in res:
    print(i)