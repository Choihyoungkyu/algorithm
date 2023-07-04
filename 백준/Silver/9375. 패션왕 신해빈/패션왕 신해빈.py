import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    dic = {}
    for _ in range(N):
        thing, kind = input().split()
        if kind not in dic:
            dic[kind] = []
        dic[kind].append(thing)
    ans = 1
    for key in dic.keys():
        ans *= (len(dic[key]) + 1)
        
    print(ans-1)