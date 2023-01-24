
N, M, P = map(int, input().split())
for i in range(P):
    if N//2 < M:
        M -= 1
    else:
        N -= 1
if N//2 >= M:
    print(M)
else:
    print(N//2)