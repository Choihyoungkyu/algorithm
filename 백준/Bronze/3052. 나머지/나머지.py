import sys
input = lambda: sys.stdin.readline().strip()

lst = []
for _ in range(10):
    N = int(input())
    lst.append(N%42)
lst = set(lst)
print(len(lst))