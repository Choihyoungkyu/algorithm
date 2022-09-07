# 골드5 / ms
import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

N, M = map(int, input().split())
lst1 = [list(map(int, input().split())) for _ in range(N)]  # 사다리
lst2 = [list(map(int, input().split())) for _ in range(M)]  # 뱀
lst1.sort()
lst2.sort()
visited = [100] * 101
visited[1] = 0
queue = deque()
queue.append(1)
while queue:
    flag = False
    t = queue.popleft()
    if t == 100:
        break

    for xi, xj in lst1:
        if t == xi and visited[xj] > visited[xi]:
            visited[xj] = visited[xi]
            queue.append(xj)
            flag = True
            break
    if flag:
        continue

    for yi, yj in lst2:
        if t == yi:
            visited[yj] = visited[yi]
            queue.append(yj)
            flag = True
            break
    if flag:
        continue

    for i in range(1, 7):
        if t+i<101 and visited[t+i] > visited[t] + 1:
            visited[t+i] = visited[t] + 1
            queue.append(t+i)

print(visited[100])
