import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
lst = [0]
for _ in range(N):
    lst.append(int(input()))

dp = [0] * (N+1)
dp[1] = lst[1]

for i in range(2,N+1):
    dp[i] = max(lst[i]+dp[i-2],lst[i]+lst[i-1] + dp[i-3])

print(dp[N])
