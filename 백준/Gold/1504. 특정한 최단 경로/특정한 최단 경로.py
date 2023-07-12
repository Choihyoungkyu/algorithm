import sys, heapq
input = sys.stdin.readline

N, E = map(int, input().split())
adjL = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adjL[a].append((c, b))
    adjL[b].append((c, a))
v1, v2 = map(int, input().split())

def dijkstra(idx):
    visited = [float('inf')] * (N+1)
    queue = []
    heapq.heappush(queue, (0, idx))
    while queue:
        cost, ci = heapq.heappop(queue)
        if visited[ci] <= cost:
            continue
        visited[ci] = cost
        for c, i in adjL[ci]:
            if visited[i] > cost + c:
                heapq.heappush(queue, (cost+c, i))
    return visited

arr1 = dijkstra(v1)
arr2 = dijkstra(v2)
answer = min(arr1[1]+arr1[v2]+arr2[N], arr2[1]+arr2[v1]+arr1[N])
print(answer if answer != float('inf') else -1)