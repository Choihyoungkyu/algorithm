import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
DP = [0] * (N+1)
DP[0] = 0
for i in range(1, N+1):
    tmp = 100
    for j in range(1, i+1):
        if j*j > i:
            break
        if DP[i - j*j] + 1 < tmp:
            tmp = DP[i - j*j] + 1
    DP[i] = tmp
print(DP[N])