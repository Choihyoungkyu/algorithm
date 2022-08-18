import sys
input = lambda: sys.stdin.readline().strip()

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

def dfs(lst, N, M):
    visited = [[N*M] * M for _ in range(N)]
    next_visit = [[0, 0, 1]]
    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 우좌하상
    visited[0][0] = 1
    result = []
    while next_visit:
        ni, nj, cnt = next_visit.pop()
        if ni == N-1 and nj == M-1:
            result.append(cnt)

        if visited[ni][nj] > cnt:
            visited[ni][nj] = cnt

        for di, dj in d:
            if 0 <= ni + di < N and 0 <= nj + dj < M:
                if lst[ni+di][nj+dj] == '1' and cnt+1 < visited[ni+di][nj+dj] : 
                    next_visit.append([ni+di, nj+dj, cnt+1])                     
        cnt += 1
    return min(result)
print(dfs(lst, N, M))