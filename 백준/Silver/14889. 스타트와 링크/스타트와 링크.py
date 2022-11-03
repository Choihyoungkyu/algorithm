# 실버2 / 
import sys
input = lambda:sys.stdin.readline().strip()

def f(cnt, k):
    global minV
    if cnt == N//2:
        s, l = 0, 0
        for y in range(N):
            for x in range(y+1, N):
                if x == y: continue
                if check[y] and check[x]:
                    s += S[y][x] + S[x][y]
                elif not check[y] and not check[x]:
                    l += S[y][x] + S[x][y]
        if abs(s-l) < minV:
            # print(f's : {s} / l : {l} / 이전 minV = {minV}')
            minV = abs(s-l)
        return
    for i in range(k, N-1):
        if not check[i]:
            check[i] = 1
            f(cnt+1, i)
            if minV == 0:
                return
            check[i] = 0

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
minV = 100*(N//2)
check = [0] * N
f(0, 0)
print(minV)
