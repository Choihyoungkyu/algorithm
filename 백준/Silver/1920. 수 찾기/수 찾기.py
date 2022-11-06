import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()

M = int(input())
M_lst = list(map(int, input().split()))

for m in M_lst:
    s = 0
    e = N-1
    while True:
        idx = (s + e) // 2
        if N_lst[idx] == m:
            print(1)
            break
        if N_lst[idx] > m:
            e = idx-1
        elif N_lst[idx] < m:
            s = idx+1
        if s > e:
            print(0)
            break