import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
lst = list(map(int, input().split()))
DP = [0] * N
DP[0] = 1
for i in range(1, N):
    tmp = 0
    for j in range(i):
        if lst[j] < lst[i] and tmp < DP[j]:
            tmp = DP[j]
    DP[i] = tmp + 1
print(max(DP))
# print(DP)