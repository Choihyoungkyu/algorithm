# 실버2 / ms
import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

a = b = c = 0
def fn(x, y, N):
    global a
    global b
    global c
    if N == 1:
        if lst[x][y] == -1:
            a += 1
            return
        elif lst[x][y] == 0:
            b += 1
            return
        else:
            c += 1
            return
    flag = False
    for i in range(N):
        for j in range(N):
            tmp = lst[x + i][y + j]
            if y + j > y and lst[x + i][y + j] != lst[x + i][y + j - 1]:
                flag = True
                break
            elif x + i > x and lst[x + i][y + j] != lst[x + i - 1][y + j]:
                flag = True
                break
        if flag:
            break
    else:
        if tmp == -1:
            a += 1
            return
        elif tmp == 0:
            b += 1
            return
        else:
            c += 1
            return
    if flag:
        for i in range(0, N, N//3):
            for j in range(0, N, N//3):
                fn(x+i, y+j, N//3)
fn(0, 0, N)
print(a)
print(b)
print(c)