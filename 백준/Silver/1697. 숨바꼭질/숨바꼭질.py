import sys
input = lambda:sys.stdin.readline().strip()

N, K = map(int, input().split())
if N >= K:
    print(abs(K-N))
else:
    lst = [100000] * (2*K+1)
    queue = []
    queue.append(N)
    lst[N] = 0
    tmp = []
    cnt = 1
    while queue:
        t = queue.pop(0)
        if t == K:
            break
        if 0<=t-1 and cnt < lst[t-1]:
            lst[t-1] = cnt
            tmp.append(t-1)
        if t+1<2*K and cnt < lst[t+1]:
            lst[t+1] = cnt
            tmp.append(t+1)
        if t <= K and cnt < lst[2*t]:
            lst[2*t] = cnt
            tmp.append(2*t)
        if queue == []:
            queue = tmp[:]
            cnt += 1
            tmp = []
    print(lst[K])