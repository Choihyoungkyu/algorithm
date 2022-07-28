import sys

N = int(sys.stdin.readline())

l = []
for i in range(N):
    x, y = map(int,sys.stdin.readline().split())
    l.append([x, y])

l.sort()

for i in range(N):
    print(l[i][0], l[i][1])