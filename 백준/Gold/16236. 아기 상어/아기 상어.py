# 골드3 / 
import sys
input = lambda:sys.stdin.readline().strip()

D = [[-1, 0], [0, -1], [0, 1], [1, 0]]

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
fish_cnt = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 9:
            fi, fj = i, j
            lst[i][j] = 0
        elif lst[i][j] != 0:
            fish_cnt += 1

time = 0
result = 0
size = 2
hunt = 0
while True:
    que = [[fi, fj, 0]]
    hunting = []
    visited = [[0] * N for _ in range(N)]
    tmp = []
    for x, y, time in que:
        if hunting and hunting[0][2] == time:
            break
        for di, dj in D:
            ni = x + di
            nj = y + dj
            if 0<=ni<N and 0<=nj<N and lst[ni][nj] <= size and visited[ni][nj] == 0:
                visited[ni][nj] = visited[x][y] + 1
                que.append([ni, nj, time+1])
                if 0 < lst[ni][nj] < size:
                    hunting.append([ni, nj, time+1])
    
    if hunting:
        hunting.sort()
        fi, fj, time = hunting[0]
        lst[fi][fj] = 0
        hunt += 1
        if hunt == size:
            size += 1
            hunt = 0
        result += time

    else:
        print(result)
        break