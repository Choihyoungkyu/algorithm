import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
lst = [float(input()) for _ in range(N)]
lst.sort()
for i in range(7):
    print(f'{lst[i]:.3f}')