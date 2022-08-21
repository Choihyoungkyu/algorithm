import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
lst = list(range(N, 0, -1))
res = []
stack = []
check = []
flag = False
for _ in range(N):
    K = int(input())
    while True:
        if len(stack) == 0:
            stack.append(lst.pop())
            check.append('+')
        if stack[-1] > K:
            flag = True
            break
        elif stack[-1] == K:
            stack.pop()
            check.append('-')
            break
        elif stack[-1] < K:
            stack.append(lst.pop())
            check.append('+')
    if flag:
        print('NO')
        break
else:
    for i in check:
        print(i)
