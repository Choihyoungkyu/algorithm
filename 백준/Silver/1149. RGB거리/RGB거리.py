import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*3 for _ in range(N)]
DP[0] = arr[0]
for i in range(1, N):
    for j in range(3):
        DP[i][j] = min(DP[i-1][(j+1)%3], DP[i-1][(j+2)%3]) + arr[i][j]
print(min(DP[N-1]))