import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

# M : 가로 칸 수, N : 세로 칸 수, H : 층 수
M, N, H = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(N)]
dic_lst = {}
dic_point = {}
dic_visited = {}
queue = deque()
num = 0
cnt = 1
for i in range(1, H+1):
    dic_lst[i] = deque(deque(map(int, input().split())) for _ in range(N))
    dic_visited[i] = deque([0]*M for _ in range(N))
    dic_point[i] = deque()
    for j in range(N):
        for k in range(M):
            if dic_lst[i][j][k] == 1:
                dic_point[i].append([j, k])
                queue.append([j, k, i])
                # dic_visited[i][j][k] = 1
            elif dic_lst[i][j][k] == 0:
                num += 1
            else:
                dic_visited[i][j][k] = -1

def DFS(dic_lst, queue):
    global num
    global cnt
    D = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]] # 북,남,동,서,상,하
    if num == 0:
        return 0
    tmp = deque()
    while queue:
        ni, nj, nk = queue.popleft()
        for di, dj, dk in D:
            if 0<=ni+di<N and 0<=nj+dj<M and 1<=nk+dk<=H and dic_lst[nk+dk][ni+di][nj+dj] == 0 and dic_visited[nk+dk][ni+di][nj+dj] == 0:
                tmp.append([ni+di, nj+dj, nk+dk])
                dic_visited[nk+dk][ni+di][nj+dj] = cnt
                num -= 1
        if queue == deque() and tmp != deque():
            queue = tmp
            cnt += 1
            tmp = deque()
    if num != 0:
        return -1
    else:
        return cnt-1
print(DFS(dic_lst, queue))
# for i in range(1, H+1):
#     for j in dic_visited[i]:
#         print(*j)