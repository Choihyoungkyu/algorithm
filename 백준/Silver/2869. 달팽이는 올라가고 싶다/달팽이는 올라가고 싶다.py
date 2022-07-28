import sys
A, B, V = map(int, sys.stdin.readline().split())
count = 0
if (V - B) % (A - B) == 0:
    print((V - B) // (A - B))
else:
    print((V - B) // (A - B) + 1)