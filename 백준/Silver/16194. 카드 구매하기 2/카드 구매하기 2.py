import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
nums = list(map(int, input().split()))
nums = [0] + nums
DP = [10000] * (N+1)
DP[0] = 0
i = 0
while i<N:
    i += 1
    for j in range(1, N+1):
        if i-j>=0:
            DP[i] = min(DP[i], DP[i-j] + nums[j])

print(DP[N])