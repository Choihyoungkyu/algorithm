import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
que = deque()
adjL_in = [[] for _ in range(N+1)]
adjL_out = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjL_in[b].append(a)
    adjL_out[a].append(b)

for i in range(1, N+1):
    if len(adjL_in[i]) == 0:
        que.append(i)

answer = []
while que:
    idx = que.popleft()
    answer.append(idx)
    
    for i in adjL_out[idx]:
        adjL_in[i].remove(idx)

    for i in adjL_out[idx]:
        if len(adjL_in[i]) == 0:
            que.append(i)

print(*answer)