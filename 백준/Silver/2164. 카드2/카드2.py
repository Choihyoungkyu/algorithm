import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

N = int(input())
lst = []

for i in range(1, N+1):
    lst.append(i)
if N == 1:
    print(1)
else:
    que = deque(lst)
    while True:
        que.popleft()
        if len(que) == 1:
            print(que[0])
            break
        que.append(que.popleft())