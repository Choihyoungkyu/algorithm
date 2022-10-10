import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()

D = [[-1, 0], [1, 0], [0, -1], [0, 1]]      # 상, 하, 좌, 우
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            Red = [i, j]
        elif arr[i][j] == 'B':
            Blue = [i, j]

def _moveBall(x, y, direction):
    cx, cy = x, y
    cnt = 0
    while True:
        nx, ny = cx + D[direction][0], cy + D[direction][1]
        if arr[nx][ny] != '#':
            cnt += 1
            cx, cy = nx, ny
            if arr[nx][ny] == 'O':
                break
        else:
            break
    return cx, cy, cnt

def moveBall(redX, redY, blueX, blueY, direction):
    n_redX, n_redY, cnt_red = _moveBall(redX, redY, direction)
    n_blueX, n_blueY, cnt_blue = _moveBall(blueX, blueY, direction)
    if n_redX == n_blueX and n_redY == n_blueY:
        if arr[n_redX][n_redY] != 'O':
            if cnt_red < cnt_blue:
                n_blueX -= D[direction][0]
                n_blueY -= D[direction][1]
            else:
                n_redX -= D[direction][0]
                n_redY -= D[direction][1]
        else:
            return redX, redY, blueX, blueY
    else:
        if arr[n_blueX][n_blueY] == 'O':
            return redX, redY, blueX, blueY
    return n_redX, n_redY, n_blueX, n_blueY

que = deque()
que.append([Red[0], Red[1], Blue[0], Blue[1], []])
cnt = 1
tmp = deque()
good = False
while cnt <= 10 and que:
    redX, redY, blueX, blueY, s = que.popleft()
    for i in range(4):
        n_redX, n_redY, n_blueX, n_blueY = moveBall(redX, redY, blueX, blueY, i)
        if arr[n_redX][n_redY] == 'O':
            good = True
            s += [i]
            break
        tmp.append([n_redX, n_redY, n_blueX, n_blueY, s+[i]])
    if good:
        break
    if que == deque() and tmp != deque():
        que = tmp
        cnt += 1
        tmp = deque()
if good:
    print(cnt)
else:
    print(-1)