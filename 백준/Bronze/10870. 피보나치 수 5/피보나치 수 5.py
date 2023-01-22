import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
DP = [0] * 21
DP[0] = 0
DP[1] = 1
for i in range(2, 21):
    DP[i] = DP[i-2] + DP[i-1]
print(DP[N])