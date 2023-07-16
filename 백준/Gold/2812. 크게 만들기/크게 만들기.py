
import sys
input = lambda: sys.stdin.readline().strip()

N, K = map(int, input().split())
num = list(map(int, input()))

stack = [num[0]]
cnt = 0
flag = False

for i in range(1, N):
    if i == K + len(stack) and len(stack) != K:
        for j in range(i,N):
            stack.append(num[j])
            flag = True
    
    if flag:
        break

    while True:
        if len(stack) == 0:
            break
        elif stack[-1] < num[i] and i != K + len(stack):
            stack.pop()
        else:
            break

    stack.append(num[i])
        
        
for i in range(N-K):
    print(stack[i], end='')