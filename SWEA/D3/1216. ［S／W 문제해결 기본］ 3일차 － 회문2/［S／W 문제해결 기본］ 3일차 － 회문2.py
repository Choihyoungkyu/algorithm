for _ in range(10):
    idx = input()
    lst = [list(input()) for _ in range(100)]
    maxV = 1
    for i in range(100):
        for j in range(100):
            for l in range(100-j+1):
                a = []
                for k in range(l//2):
                    if lst[i][j + k] == lst[i][j + l - 1 - k]:  # 가로 회문 찾기
                        pass
                    else:
                        break
                else:
                    a = lst[i][j:j + l]  # 찾은 회문 저장
                    if maxV < len(a):
                        maxV = len(a)
                      
                a = []
                for k in range(l // 2):  # 세로 회문 찾기
                    if lst[j + k][i] == lst[j + l - 1 - k][i]:
                        pass
                    else:
                        break
                else:
                    for m in range(l):  # 찾은 회문 저장
                        a.append(lst[j + m][i])
                    if maxV < len(a):
                        maxV = len(a)

    print(f'#{idx} {maxV}')

