import sys
input = lambda: sys.stdin.readline().strip()

lst = list(input())
tar = list(input())
l = len(tar)

stack = []
for i in range(len(lst)):
    stack.append(lst[i])
    if stack[-1] == tar[-1] and stack[-l:] == tar:  
        for _ in range(l):
            stack.pop()        

if len(stack) != 0:
    for i in stack:
        print(i, end='')
else:
    print('FRULA')