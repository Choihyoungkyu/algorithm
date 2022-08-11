import sys
input = lambda: sys.stdin.readline().strip()
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    else: 
        print(N+M)