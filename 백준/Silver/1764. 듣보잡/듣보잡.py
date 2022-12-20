import sys
input = lambda:sys.stdin.readline().strip()

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    s = input()
    dic[s] = 1
lst = []
for _ in range(M):
    s = input()
    if s in dic:
        lst.append(s)
lst.sort()
print(len(lst))
for s in lst:
    print(s)