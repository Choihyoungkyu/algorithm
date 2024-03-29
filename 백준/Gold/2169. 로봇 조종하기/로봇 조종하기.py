import sys

input = sys.stdin.readline

N, M = map(int, input().split())
D = ((0, -1), (0, 1), (1, 0))                           # Left, Right, Down
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * M for _ in range(N)]
DP[0][0] = arr[0][0]
for j in range(1, M):
    DP[0][j] = DP[0][j-1] + arr[0][j]

i = 0

while i<N-1:
    i += 1
    left_tmp, right_tmp = [0] * M, [0] * M
    # 왼쪽으로
    left_tmp[M-1] = DP[i-1][M-1] + arr[i][M-1]
    for j in range(M-2, -1, -1):
        left_tmp[j] = max(DP[i-1][j], left_tmp[j+1]) + arr[i][j]
    
    # 오른쪽으로
    right_tmp[0] = DP[i-1][0] + arr[i][0]
    for j in range(1, M):
        right_tmp[j] = max(DP[i-1][j], right_tmp[j-1]) + arr[i][j]

    # 합치기
    for j in range(M):
        DP[i][j] = max(left_tmp[j], right_tmp[j])

print(DP[N-1][M-1])