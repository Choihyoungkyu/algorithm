import sys
T = int(input())
for tc in range(T):
    N = int(input())
    Numbers = [list(map(int, input().split())) for _ in range(2)]
    DP = [[0] * N for _ in range(2)]
    DP[0][0], DP[1][0] = Numbers[0][0], Numbers[1][0]
    
    if N == 1:
        print(max(DP[0][0], DP[1][0]))
        continue

    for i in range(1, N):
        if i == 1:
            DP[0][i], DP[1][i] = Numbers[0][i] + DP[1][i-1], Numbers[1][i] + DP[0][i-1]
        else:
            DP[0][i] = max(DP[1][i-1]+Numbers[0][i], DP[1][i-2]+Numbers[0][i])
            DP[1][i] = max(DP[0][i-1]+Numbers[1][i], DP[0][i-2]+Numbers[1][i])
        if i == N-1:
            max_v = max(DP[0][N-1], DP[1][N-1])

    print(max_v)