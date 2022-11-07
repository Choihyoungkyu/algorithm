import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
Tensions = [int(input()) for _ in range(N)]
Tensions.sort(reverse=True)
maxV = 0
for i in range(N):
    if Tensions[i] * (i+1) < maxV:
        if N * Tensions[i] < maxV:
            break
    if maxV < Tensions[i] * (i+1):
        maxV = Tensions[i] * (i+1)
print(maxV)