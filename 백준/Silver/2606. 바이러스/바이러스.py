import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

T = int(input())
N = int(input())

graph = [[] for _ in range(T+1)]
for i in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [0] * (T + 1)

def bfs(graph, start, visited):
    cnt = 0
    queue = graph[start]
    visited[start] = 1

    while queue:                            # while -> 새로 들어오는 값들을 탐색
        pop = queue.pop(0)
        visited[pop] = 1
        for e in graph[pop]:
            if not visited[e]:
                queue.append(e)
                visited[e] = 1
                
    if visited[1] == 1:
        for i in range(T+1):
            if visited[i] == 1:
                cnt += 1
        print(cnt-1)
    else:
        print(0)
bfs(graph, 1, visited)