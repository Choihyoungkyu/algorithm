from collections import deque

def solution(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
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
    dfs(1, 0)
    print(res)
    answer = max(res)
    return answer