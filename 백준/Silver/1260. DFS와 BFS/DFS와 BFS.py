import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()

N, M, V = map(int, input().split())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    num1, num2 = map(int, input().split())
    adjL[num1].append(num2)
    adjL[num2].append(num1)

for idx in range(N+1):
    adjL[idx].sort()

def DFS(V):
    stack = []
    result = [V]
    visited = [0] * (N+1)
    visited[V] = 1
    while True:
        for idx in adjL[V]:
            if visited[idx] == 0:
                visited[idx] = 1
                stack.append(V)
                result.append(idx)
                V = idx
                break
        else:
            if not stack:
                break
            else:
                V = stack.pop()
    return result

# print(adjL)
def BFS(V):
    que = deque()
    que.append(V)
    visited = [0] * (N+1)
    visited[V] = 1
    result = [V]
    while que:
        V = que.popleft()
        for idx in adjL[V]:
            if visited[idx] == 0:
                visited[idx] = 1
                que.append(idx)
                result.append(idx)
    return result

print(*DFS(V))
print(*BFS(V))