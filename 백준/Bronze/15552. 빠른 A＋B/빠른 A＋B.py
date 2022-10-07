import sys
input = lambda:sys.stdin.readline().strip()

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a+b)