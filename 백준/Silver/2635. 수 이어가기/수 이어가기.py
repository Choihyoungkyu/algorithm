import sys

input = lambda: sys.stdin.readline().strip()
x= int(input())

cnt = 0
for i in range(int(x//2), x+1):
    num = [x]
    num.append(i)
    j = 0
    tmp = 0
    while num[-1] >= 0:
        num.append(num[j] - num[j+1])
        j += 1
    tmp = len(num)
    if tmp > cnt:
        cnt = len(num) - 1
        idx = i
print(cnt)
num = [x]
num.append(idx)
j = 0
while num[-1] >= 0:
    num.append(num[j] - num[j+1])
    j += 1
num.pop()
for i in num:
    print(i, end=' ')