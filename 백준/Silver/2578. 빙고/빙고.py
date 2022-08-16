import sys
input = lambda: sys.stdin.readline().strip()

bingo = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
bing = 0
lst = [[],[],[],[]] # 이미 체크한 줄(가로, 세로, 대각1, 대각2)

flag = False
for _ in range(5):
    call = list(map(int, input().split()))
    for k in call:    
        for i in range(5):
            if k in bingo[i]:
                tmp = bingo[i].index(k)
                bingo[i][tmp] = 0
                cnt += 1
                
                for j in range(5):                  # 가로
                    if bingo[i][j] == 0:
                        pass
                    else:
                        break
                else:
                    if i not in lst[0]:
                        bing += 1
                        lst[0].append(i)
                    if bing >= 3:
                        flag = True
                        break

                for j in range(5):                  # 세로
                    if bingo[j][tmp] == 0:
                        pass
                    else:
                        break
                else:
                    if tmp not in lst[1]:
                        bing += 1
                        lst[1].append(tmp)
                    if bing >= 3:
                        flag = True
                        break

                for j in range(5):                  # 대각선 1
                    if bingo[j][j] == 0:
                        pass
                    else:
                        break
                else:
                    if 0 not in lst[2]:
                        bing += 1
                        lst[2].append(0)
                    if bing >= 3:
                        flag = True
                        break

                for j in range(5):                  # 대각선 2
                    if bingo[j][4-j] == 0:
                        pass
                    else:
                        break
                else:
                    if 0 not in lst[3]:
                        bing += 1
                        lst[3].append(0)
                    if bing >= 3:
                        flag = True
                        break

            if flag == True:
                break
        if flag == True:
            break
    if flag == True:
        break

print(cnt)