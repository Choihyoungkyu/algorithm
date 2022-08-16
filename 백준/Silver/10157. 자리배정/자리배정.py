C, R = map(int, input().split())
lst = [[0]*C for _ in range(R)]  # RxC 행렬 생성
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 하좌상우

lst[R-1][0] = 1

row = R-1
col = 0

cnt = 2
rot = 0
key = int(input())

if key == 1:
    print('1 1')
elif key <= C*R:
    while cnt <= C*R:
        if 0 <= row + d[rot][0] < R and 0 <= col + d[rot][1] < C:
            if lst[row + d[rot][0]][col + d[rot][1]] == 0:
                lst[row + d[rot][0]][col + d[rot][1]] = cnt
                row += d[rot][0]
                col += d[rot][1]
                if cnt == key:
                    print(col + 1, R - row)
                    break
                cnt += 1
            else:
                rot = (rot + 1) % 4
        else:
            rot = (rot + 1) % 4
else:
    print(0)
