import sys

input = lambda: sys.stdin.readline().strip()
N = int(input())
m = []
for i in range(1001):
    b = []
    for j in range(1001):
        b.append(0)
    m.append(b)

for k in range(N):
    a, b, c, d = map(int, input().split())
    for j in range(a, a+c):
        for i in range(b, b+d):
            m[j][i] = k + 1

for i in range(1,N+1):
    count = 0
    for k in m:
        for s in k:
            if i == s:
                count += 1
    print(count)