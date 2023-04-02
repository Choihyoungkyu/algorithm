import sys
input = lambda : sys.stdin.readline().strip()

stack1 = []
stack2 = []
res = []
s = list(input())
string = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(len(s)):
    if s[i] in string:
        res.append(s[i])
    else:
        if not stack1:
            stack1.append(s[i])
        elif s[i] == '(':
            stack1.append(s[i])
        elif s[i] == '*' or s[i] == '/':
            while stack1 and stack1[-1] != '(' and stack1[-1] != '+' and stack1[-1] != '-':
                res.append(stack1.pop())
            stack1.append(s[i])
        elif s[i] == '+' or s[i] == '-':
            while stack1 and stack1[-1] != '(':
                res.append(stack1.pop())
            stack1.append(s[i])
        elif s[i] == ')':
            while stack1 and stack1[-1] != '(':
                res.append(stack1.pop())
            stack1.pop()
while stack1:
    res.append(stack1.pop())

for i in res:
    print(i, end='')