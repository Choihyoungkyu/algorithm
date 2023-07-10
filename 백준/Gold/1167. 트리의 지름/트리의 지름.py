import sys, heapq
input = sys.stdin.readline

N = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(N):
    n, *lst = map(int, input().split())
    for i in range(0, len(lst), 2):
        if lst[i] == -1:
            break
        adjL[n].append((-lst[i+1], lst[i]))

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

arr1 = dijkstra(1)
print(-min(dijkstra(arr1.index(min(arr1)))))