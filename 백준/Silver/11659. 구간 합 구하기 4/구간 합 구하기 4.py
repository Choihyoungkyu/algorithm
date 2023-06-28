import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Numbers = list(map(int, input().split()))
DP = [0] * (N+1)
for i in range(1, N+1):
    DP[i] += DP[i-1] + Numbers[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(DP[j]-DP[i-1])