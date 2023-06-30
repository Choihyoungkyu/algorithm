from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Map = [list(input().strip()) for _ in range(N)]

def BFS():
    D = ((0, 1), (0, -1), (1, 0), (-1, 0))
    visited_possible = [[0] * M for _ in range(N)]
    visited_impossible = [[0] * M for _ in range(N)]
    visited_possible[0][0] = 1
    queue = deque()
    queue.append((0, 0, True))
    while queue:
        ci, cj, is_possible = queue.popleft()
        if ci == N-1 and cj == M-1:
            return max(visited_possible[ci][cj], visited_impossible[ci][cj])
        for di, dj in D:
            ni, nj = ci+di, cj+dj
            if is_possible:
                if 0<=ni<N and 0<=nj<M and not visited_possible[ni][nj]:
                    if Map[ni][nj] == '0':
                        visited_possible[ni][nj] = visited_possible[ci][cj]+1
                        queue.append((ni, nj, is_possible))
                    else:
                        visited_impossible[ni][nj] = visited_possible[ci][cj]+1
                        queue.append((ni, nj, False))
            else:
                if 0<=ni<N and 0<=nj<M and not visited_impossible[ni][nj] and Map[ni][nj] == '0':
                    visited_impossible[ni][nj] = visited_impossible[ci][cj]+1
                    queue.append((ni, nj, is_possible))


ans = BFS()
print(ans if ans else -1)