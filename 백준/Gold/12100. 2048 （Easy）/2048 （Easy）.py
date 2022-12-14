from copy import deepcopy
import sys
input = lambda:sys.stdin.readline().strip()

def up(arr):
    global maxV
    for i in range(N):
        for j in range(N-1):
            for k in range(j+1, N):
                if arr[k][i] != 0:
                    if arr[j][i] == 0 or arr[k][i] == arr[j][i]:
                        if arr[j][i] == 0:
                            for l in range(k+1, N):
                                if arr[l][i] != 0:
                                    if arr[l][i] == arr[k][i]:
                                        arr[j][i] += arr[l][i]
                                        arr[l][i] = 0
                                    break
                        arr[j][i] += arr[k][i]
                        arr[k][i] = 0
                    break
            if maxV < arr[j][i]:
                maxV = arr[j][i]

def down(arr):
    global maxV
    for i in range(N):
        for j in range(N-1, 0, -1):
            for k in range(j-1, -1, -1):
                if arr[k][i] != 0:
                    if arr[j][i] == 0 or arr[k][i] == arr[j][i]:
                        if arr[j][i] == 0:
                            for l in range(k-1, -1, -1):
                                if arr[l][i] != 0:
                                    if arr[l][i] == arr[k][i]:
                                        arr[j][i] += arr[l][i]
                                        arr[l][i] = 0
                                    break
                        arr[j][i] += arr[k][i]
                        arr[k][i] = 0
                    break
            if maxV < arr[j][i]:
                maxV = arr[j][i]

def left(arr):
    global maxV
    for i in range(N):
        for j in range(N-1):
            for k in range(j+1, N):
                if arr[i][k] != 0:
                    if arr[i][j] == 0 or arr[i][k] == arr[i][j]:
                        if arr[i][j] == 0:
                            for l in range(k+1, N):
                                if arr[i][l] != 0:
                                    if arr[i][l] == arr[i][k]:
                                        arr[i][j] += arr[i][l]
                                        arr[i][l] = 0
                                    break
                        arr[i][j] += arr[i][k]
                        arr[i][k] = 0
                    break
            if maxV < arr[i][j]:
                maxV = arr[i][j]

def right(arr):
    global maxV
    for i in range(N):
        for j in range(N-1, 0, -1):
            for k in range(j-1, -1, -1):
                if arr[i][k] != 0:
                    if arr[i][j] == 0 or arr[i][k] == arr[i][j]:
                        if arr[i][j] == 0:
                            for l in range(k-1, -1, -1):
                                if arr[i][l] != 0:
                                    if arr[i][l] == arr[i][k]:
                                        arr[i][j] += arr[i][l]
                                        arr[i][l] = 0
                                    break
                        arr[i][j] += arr[i][k]
                        arr[i][k] = 0
                    break
            if maxV < arr[i][j]:
                maxV = arr[i][j]

def f(arr, cnt):
    if cnt == 5:
        return 
    else:
        tmp_arr = deepcopy(arr)
        up(tmp_arr)
        f(tmp_arr, cnt+1)

        tmp_arr = deepcopy(arr)
        down(tmp_arr)
        f(tmp_arr, cnt+1)

        tmp_arr = deepcopy(arr)
        left(tmp_arr)
        f(tmp_arr, cnt+1)

        tmp_arr = deepcopy(arr)
        right(tmp_arr)
        f(tmp_arr, cnt+1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
maxV = 0
for i in range(N):
    for j in range(N):
        if maxV < arr[i][j]:
            maxV = arr[i][j]
f(arr, cnt)
print(maxV)
