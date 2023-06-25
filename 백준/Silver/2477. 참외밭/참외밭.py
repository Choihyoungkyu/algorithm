import sys
input = lambda: sys.stdin.readline().strip()

K = int(input())  # K : 참외의 개수

X = []
Y = []
lst = []

for _ in range(6):
    a, b = map(int, input().split())
    lst.append(b)
    if a == 1 or a == 2:
        X.append(b)
        first = 'y'
    elif a == 3 or a == 4:
        Y.append(b)
        first = 'x'

max_x = max(X)
max_y = max(Y)
min_x = lst[lst.index(max_y)-1] if lst[lst.index(max_y)-1] != max_x else lst[(lst.index(max_y) + 1) % 6]
min_y = lst[lst.index(max_x)-1] if lst[lst.index(max_x)-1] != max_y else lst[(lst.index(max_x) + 1) % 6]

res = max_x * max_y - (max_x-min_x) * (max_y-min_y)
print(res*K)