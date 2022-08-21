import sys
input = lambda: sys.stdin.readline().strip()

s = list(input())
stack = []
cnt = 0
for i in range(len(s)):
    if i != 0 and s[i-1] == '(' and s[i] == ')':
        stack.pop()
        cnt += len(stack)
        
    elif s[i] == ')':
        stack.pop()
        cnt += 1
        
    else:
        stack.append(s[i])
print(cnt)