import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
lst = []
for _ in range(N):
    a, b = input().split()
    lst.append([int(a), b])
lst.sort(key=lambda x:x[0])
for a, b in lst:
    print(a, b)