from collections import deque

def solution(info, edges):
    answer = 0
    adjL = [[] for _ in range(len(info))]
    for edge in edges:
        adjL[edge[0]].append(edge[1])
        adjL[edge[1]].append(edge[0])
    visited = [0] * len(info)
    visited[0] = 1
    s = 1
    w = 0
    res = []
    def dfs(s, w):
        if s > w:
            res.append(s)
        else:
            return 
        
        for n1, n2 in edges:
            if visited[n1] and not visited[n2]:
                visited[n2] = 1
                if info[n2] == 0:
                    dfs(s+1, w)
                else:
                    dfs(s, w+1)
                visited[n2] = 0
    dfs(s, w)
    print(res)
    answer = max(res)
    return answer