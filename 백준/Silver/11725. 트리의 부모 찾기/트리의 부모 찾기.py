n = int(input())
nodes = {i: [] for i in range(1, n+1)}
visited = [0 for i in range(n+1)]
for i in range(n-1):
    a, b = list(map(int, input().split()))
    if b not in nodes[a]:
        nodes[a].append(b)
    if a not in nodes[b]:
        nodes[b].append(a)

def bfs():
    visited[1] = 1
    next = [1]
    while True:
        if len(next) == 0: break
        idx = next.pop(0)
        for node in nodes[idx]:
            if visited[node] == 0:
                next.append(node)
                visited[node] = idx

bfs()
for i in range(2, n+1):
    print(visited[i])