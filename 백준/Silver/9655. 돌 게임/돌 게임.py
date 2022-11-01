import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
DP = [0] * N
if N > 6 or N == 3 or N == 5:
    DP[0] = N-3
else:
    DP[0] = N-1
idx = 0
if DP[0] <= 0:
    pass
else:
    for i in range(1, N):
        if DP[i-1] > 6 or DP[i-1] == 3 or DP[i-1] == 5:
            DP[i] = DP[i-1]-3
        else:
            DP[i] = DP[i-1]-1
        if DP[i] == 0:
            idx = i
            # print(DP)
            break
if idx % 2 == 0:
    print('SK')
else:
    print('CY')