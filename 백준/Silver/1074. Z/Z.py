import sys
input = lambda : sys.stdin.readline().strip()

def f(N, ni1, nj1):
    global cnt
    if N == 1:
        cnt -= 1
        for i in range(2):
            for j in range(2):
                cnt += 1
                if ni1+i == r and nj1+j == c:
                    return cnt
    else:
        ni1, ni2 = ni1, ni1 + (2**N) - (2**(N-1))
        nj1, nj2 = nj1, nj1 + (2**N) - (2**(N-1))
        N -= 1
        if r < ni1 + 2**N and c < nj1 + 2**N:
            f(N, ni1, nj1)
        elif r < ni1 + 2**N and c >= nj1 + 2**N:
            cnt += ((2**N)**2)
            f(N, ni1, nj2)
        elif r >= ni1 + 2**N and c < nj1 + 2**N:
            cnt += ((2**N)**2) * 2
            f(N, ni2, nj1)
        elif r >= ni1 + 2**N and c >= nj1 + 2**N:
            cnt += ((2**N)**2) * 3
            f(N, ni2, nj2)

N, r, c = map(int, input().split())
cnt = 0
f(N, 0, 0)
print(cnt)