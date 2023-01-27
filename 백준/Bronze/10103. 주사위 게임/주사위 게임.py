import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
a, b = 100, 100
for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        b -= A
    elif B > A:
        a -= B
print(a)
print(b)