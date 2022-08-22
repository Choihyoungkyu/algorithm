import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
lst = list(map(int, input().split()))
stack = []
res = [-1] * N

stack.append(0)
for i in range(1, N):
    # 방법 1
    # M = len(stack)
    # for _ in range(M):
    #     if lst[stack[-1]] < lst[i]:
    #         res[stack.pop()] = lst[i]
    # stack.append(i)

    # 방법 2
    while stack and lst[i] > lst[stack[-1]]:
        res[stack.pop()] = lst[i]
    stack.append(i)

print(*res)