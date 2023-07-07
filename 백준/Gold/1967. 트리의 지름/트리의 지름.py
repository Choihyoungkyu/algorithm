import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    adjL[a].append([c, b])

Tree = [[0, 0] for _ in range(N+1)]
maxV = 0

new_adjL = [[] for _ in range(N+1)]
visited = [0] * (N+1)
que = deque()
que.append(1)
dic = {}
while que:
    idx = que.popleft()
    if visited[idx]: continue

    visited[idx] = 1
    for i in range(1, N+1):
        if not new_adjL[i]:
            new_adjL[i] = adjL[idx]
            dic[idx] = i
            break

    for c, i in adjL[idx]:
        if not visited[i]:
            que.append(i)

def func(idx, maxV):
    tmp = 0
    lst = []
    for c, i in new_adjL[idx]:
        i = dic[i]
        c += Tree[i][1]
        lst.append(c)
        tmp = max(tmp, c)
    lst.sort(reverse=True)
    Tree[idx] = [sum(lst[:2]), tmp]
    return max(sum(lst[:2]), tmp, maxV)

for i in range(N, 0, -1):
    maxV = func(i, maxV)
print(maxV)
