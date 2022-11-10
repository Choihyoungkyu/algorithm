A, B = map(int, input().split())
num = 1
tmp = 0
tot = 0
for i in range(B):
    if A-1 <= i < B:
        tot += num
    tmp += 1
    if num == tmp:
        num += 1
        tmp = 0
print(tot)