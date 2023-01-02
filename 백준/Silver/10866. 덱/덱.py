import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()


def f(s, num, que):
    if s == "push_front":
        que.appendleft(num)
    elif s == "push_back":
        que.append(num)
    elif s == "pop_front":
        try:
            print(que.popleft())
        except:
            print(-1)
    elif s == "pop_back":
        try:
            print(que.pop())
        except:
            print(-1)
    elif s == "size":
        print(len(que))
    elif s == "empty":
        if len(que):
            print(0)
        else:
            print(1)
    elif s == "front":
        try:
            print(que[0])
        except:
            print(-1)
    elif s == "back":
        try:
            print(que[-1])
        except:
            print(-1)

que = deque()
N = int(input())
for _ in range(N):
    tmp = input()
    lst = tmp.split(" ")
    if len(lst) == 1:
        f(lst[0], 0, que)
    else:
        f(lst[0], int(lst[1]), que)
    