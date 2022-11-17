import sys
input = lambda:sys.stdin.readline().strip()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
tot = 0
for i in range(N):
    for j in range(i, N):
        tot += lst[j]
        if tot > M:
            tot = 0
            break
        elif tot == M:
            cnt += 1
            tot = 0
            break
    else:
        tot = 0
print(cnt)