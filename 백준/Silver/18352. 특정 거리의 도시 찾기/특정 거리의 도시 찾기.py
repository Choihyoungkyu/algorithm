from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjL[a].append(b)

visited = [float('inf')] * (N + 1)
answer = []

def bfs():
    que = deque([(X, 0)])
    visited[X] = 0
    
    while que:
        idx, cost = que.popleft()
        
        for i in adjL[idx]:
            if visited[i] > cost + 1:
                visited[i] = cost + 1
                if cost + 1 == K: 
                    answer.append(i)
                elif cost + 1 < K: 
                    que.append((i, cost + 1))

bfs()
if answer:
    for i in sorted(answer):
        print(i)
else:
    print(-1)
