import sys
input = lambda:sys.stdin.readline().strip()

lst = list(map(int, input()))
if 0 in lst:
    if sum(lst) % 3 == 0:
        lst.sort(reverse=True)
        for i in lst:
            print(i, end='')
    else:
        print(-1)
else:
    print(-1)