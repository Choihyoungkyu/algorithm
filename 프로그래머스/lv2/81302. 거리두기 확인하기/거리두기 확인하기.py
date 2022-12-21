def DFS(places, idx):
    D = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(5):
        for j in range(5):
            if places[idx][i][j] != "P":
                continue
            visited = list([0]*5 for _ in range(5))
            stack = []
            ci, cj = i, j
            visited[ci][cj] = 1
            cnt = 1
            while True:
                if cnt < 3:
                    for di, dj in D:
                        ni, nj = ci+di, cj+dj
                        if 0<=ni<5 and 0<=nj<5 and visited[ni][nj] == 0:
                            if places[idx][ni][nj] == "O":
                                cnt += 1
                                visited[ni][nj] = cnt
                                stack.append([ci, cj])
                                ci, cj = ni, nj
                                break
                            elif places[idx][ni][nj] == "P":
                                return 0
                    else:
                        if stack:
                            pos = stack.pop()
                            ci, cj = pos[0], pos[1]
                            cnt -= 1
                        else:
                            break
                else:
                    if stack:
                        pos = stack.pop()
                        ci, cj = pos[0], pos[1]
                        cnt -= 1
                    else:
                        break
    return 1

def solution(places):
    answer = []
    # for i in places:
    #     for j in i:
    #         print(j)
    #     print()
    for i in range(5):
        answer.append(DFS(places, i))
    
    return answer