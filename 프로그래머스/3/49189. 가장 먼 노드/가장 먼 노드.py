from collections import deque

def solution(n, edge):
    answer = 0
    adjL = [[] for _ in range(n+1)]
    for a, b in edge:
        adjL[a].append(b)
        adjL[b].append(a)

    visited = [float('inf')] * (n+1)
    visited[0] = 0
    visited[1] = 0
    idx_lst = deque()
    idx_lst.append(1)

    while idx_lst:
        idx = idx_lst.popleft()
        for i in adjL[idx]:
            if visited[i] > visited[idx] + 1:
                visited[i] = visited[idx] + 1
                idx_lst.append(i)

    answer = visited.count(max(visited))
    return answer