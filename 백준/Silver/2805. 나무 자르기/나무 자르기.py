import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Trees = list(map(int, input().split()))
Trees.sort()

s, e = 0, Trees[N-1]
while s<=e:
    m = (s+e)//2
    tot = 0
    for tree in Trees:
        if tree > m:
            tot += tree - m
    if tot >= M:
        s = m+1
    elif tot < M:
        e = m-1
print(e)