tot = int(input())
n = int(input())
tmp = 0
for _ in range(n):
    a, b = map(int, input().split())
    tmp += a * b
if tot == tmp:
    print('Yes')
else:
    print('No')
    