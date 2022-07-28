import sys

s = sys.stdin.readline()

l = []
for i in s:
    l.append(i)
l.sort(reverse=True)
for i in l:
    print(i, end='')