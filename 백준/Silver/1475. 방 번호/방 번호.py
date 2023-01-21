import sys
input = lambda:sys.stdin.readline().strip()

N = input()
dic = {}
for i in range(10):
    dic[i] = 0

for i in N:
    i = int(i)
    if i == 6 or i == 9:
        if dic[6] <= dic[9]:
            dic[6] += 1
        else:
            dic[9] += 1
    else:
        dic[i] += 1

maxV = 0
for value in dic.values():
    maxV = max(maxV, value)
print(maxV)