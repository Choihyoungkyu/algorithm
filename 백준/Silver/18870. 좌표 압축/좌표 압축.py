import sys
input = lambda:sys.stdin.readline().strip()

def bin_search(s, e, n):
    global tmp
    m = (s + e) // 2
    if n == Y[m]:
        tmp = m
        return
    if n < Y[m]:
        e = m - 1
        bin_search(s, e, n)
    elif n > Y[m]:
        s = m + 1
        bin_search(s, e, n)
    else:
        tmp = 0
        return 
    
N = int(input())
X = list(map(int, input().split()))
Y = sorted(list(set(X)))
ans = [0] * N
dic = {}
for i in range(N):
    if X[i] in dic:
        ans[i] = dic[X[i]]
        continue
    tmp = 0
    bin_search(0, len(Y)-1, X[i])
    ans[i] = tmp
    dic[X[i]] = tmp
print(*ans)