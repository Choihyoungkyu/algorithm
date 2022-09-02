import sys
input = lambda:sys.stdin.readline().strip()
from copy import deepcopy
from collections import deque

N = int(input())
lst = []
for _ in range(N):
    S, E = map(int, input().split())
    lst.append([S, E])
lst.sort()

visited = deque([lst[0]])
cnt = 1
i = 1
j = 0
while i != N:
    if lst[i][1] < visited[-1][1]:
        visited.pop()
        visited.append(lst[i])
        j = i
        i -= 1
    elif lst[i][0] >= visited[-1][1]:
        if i != j:
            visited.append(lst[i])
            j = i
            i += 1
        else:
            i += 1
    elif lst[i][0] < visited[-1][1]:
        i += 1

print(len(visited))
