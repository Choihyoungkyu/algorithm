import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
M = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adjL[a].append((c, b))
for i in range(1, N+1):
    adjL[i].sort()
start, end = map(int, input().split())

def dijkstra(start, end, adjL, N):
    if start == end: return 0
    
    visited = [float('inf')] * (N+1)
    visited[start] = 0
    que = []
    heappush(que, (0, start))
    while que:
        cost, current = heappop(que)
        if visited[current] < cost: continue
        
        for value, idx in adjL[current]:
            if visited[idx] > cost + value:
                visited[idx] = cost + value
                heappush(que, (cost + value, idx))
                
    return visited[end]

print(dijkstra(start, end, adjL, N))