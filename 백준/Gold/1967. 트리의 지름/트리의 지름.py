import sys, heapq
input = sys.stdin.readline

N = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    adjL[a].append((-c, b))
    adjL[b].append((-c, a))

def dijkstra(i):
    queue = []
    heapq.heappush(queue, (0, i))
    visited = [1] * (N+1)
    while queue:
        cost, idx = heapq.heappop(queue)
        if visited[idx] != 1:
            continue
        visited[idx] = cost
        for c, i in adjL[idx]:
            if visited[i] == 1:
                heapq.heappush(queue, (cost + c, i))
    return visited

answer = 0
arr1 = dijkstra(1)
print(-min(dijkstra(arr1.index(min(arr1)))))