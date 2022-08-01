import sys

N = int(sys.stdin.readline())
i = 1
l = []
while i <= N:
    s = sys.stdin.readline().rstrip()
    if s.find(' ') != -1:
        l.append(int(s[s.find(' ')+1:]))
        i += 1
    elif s == 'pop':
        if len(l) == 0:
            print(-1)
        else:
            print(l.pop())
        i += 1
    elif s == 'size':
        print(len(l))
        i += 1
    elif s == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)
        i += 1
    elif s == 'top':
        if len(l) == 0:
            print(-1)
        else:
            print(l[-1])
        i += 1