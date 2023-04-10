# import sys

# input = lambda: sys.stdin.readline().strip

N = int(input())
num = list(map(int, input().split()))
lst = []

if N == 1:
    lst = [1]
else:
    for i in range(N-1):
        if num[i] - num[i+1] > 0:
            lst.append(1)
        elif num[i] - num[i+1] < 0:
            lst.append(-1)
        else:
            lst.append(0)
posi = 0
negi = 0
if lst[0] == 1:
    posi = 1
elif lst[0] == -1:
    negi = 1
else:
    posi = 1
    negi = 1
cnt = 0
for i in range(1, N-1):
    if lst[i] == 1:
        negi = 0
        posi += 1
        if posi >= cnt:
            cnt = posi
    elif lst[i] == -1:
        posi = 0
        negi += 1
        if negi >= cnt:
            cnt = negi
    else:
        posi += 1
        negi += 1
        if posi >= cnt:
            cnt = posi
        elif negi >= cnt:
            cnt = negi
print(cnt+1)