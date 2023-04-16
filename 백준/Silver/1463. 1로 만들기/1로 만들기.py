import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())

l = [0] * 1000001
l[2] = 1
l[3] = 1
for i in range(4, N+1):
    a = b = c = i
    if i % 2 == 0:
        a = l[i//2] + 1 
    if i % 3 == 0:
        b = l[i//3] + 1 
    c = l[i-1] + 1
    l[i] = min(a, b, c)

print(l[N])