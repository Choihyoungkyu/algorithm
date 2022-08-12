import sys
input = lambda: sys.stdin.readline().strip()

DP = [[0,0] for _ in range(41)]
DP[0] = [1, 0]
DP[1] = [0, 1]

N = int(input())
for i in range(N):
    a = int(input())
    for i in range(2, a+1):
        DP[i][0] = DP[i-1][0] + DP[i-2][0]
        DP[i][1] = DP[i-1][1] + DP[i-2][1]
    print(*DP[a])