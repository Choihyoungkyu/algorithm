import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
lst = [0] * 12
lst[1] = 1
lst[2] = 2
lst[3] = 4
for i in range(4, 12):
    lst[i] = lst[i-3] + lst[i-2] + lst[i-1]
    
for _ in range(N):
    n = int(input())
    print(lst[n])