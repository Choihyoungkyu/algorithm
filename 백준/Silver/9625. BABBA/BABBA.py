N = int(input())
DP = [[0, 0] for _ in range(N+1)]
DP[0] = [1, 0]
for i in range(1, N+1):
    DP[i] = [DP[i-1][1], sum(DP[i-1])]
print(*DP[N])