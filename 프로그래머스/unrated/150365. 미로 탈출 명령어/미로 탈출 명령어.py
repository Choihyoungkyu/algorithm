from collections import deque

def BFS(n, m, x, y, r, c, k):
    D = [['d', 1, 0], ['l', 0, -1], ['r', 0, 1], ['u', -1, 0]]
    ci, cj = x, y
    que = deque()
    que.append(['', 0, ci, cj])
    res = []
    while que:
        cs, cnt, ci, cj = que.popleft()
        if ci == r and cj == c and cnt == k:
            res.append(cs)
            continue
        for ds, di, dj in D:
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and abs(ni-r)+abs(nj-c)+cnt+1 <= k:
                que.append([cs+ds, cnt+1, ni, nj])
                break
    return res

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    if (abs(x-r)+abs(y-c)) % 2 != k % 2 or abs(x-r)+abs(y-c) > k: return 'impossible'
    answer = BFS(n, m, x-1, y-1, r-1, c-1, k)
    

    return answer[0]