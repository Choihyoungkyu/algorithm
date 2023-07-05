import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K, *Knows = list(map(int, input().split()))
Parties = [[] for _ in range(M)]
adjL = [[] for _ in range(N+1)]
for _ in range(M):
    n, *lst = list(map(int, input().split()))
    Parties[_] = lst
    for i in range(n-1):
        for j in range(i, n):
            if lst[j] != lst[i] and lst[j] not in adjL[lst[i]]:
                adjL[lst[i]].append(lst[j])
            if lst[i] != lst[j] and lst[i] not in adjL[lst[j]]:
                adjL[lst[j]].append(lst[i])

visited = [0] * (N+1)

def func(idx):
    visited[idx] = 1
    for i in adjL[idx]:
        if not visited[i]:
            func(i)

for k in Knows:    
    if not visited[k]:
        func(k)

answer = 0

for party in Parties:
    for i in party:
        if visited[i]:
            break
    else:
        answer += 1

print(answer)