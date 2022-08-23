import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
# lst = [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
tot = 0                   
maxV = 0                                                                                        
stack = [0]*(lst[-1][0]+1)
for i in range(N):
    if maxV < lst[i][1]:
        maxV = lst[i][1]
        idx = lst[i][0]

tmp = 0
for i in range(N):
    stack[lst[i][0]] = lst[i][1]

for i in range(idx+1):
    if stack[i] > tmp:
        tmp = stack[i]
    tot += tmp
tmp = 0 
for i in range(lst[-1][0], idx, -1):
    if stack[i] > tmp:
        tmp = stack[i]
    tot += tmp
print(tot)