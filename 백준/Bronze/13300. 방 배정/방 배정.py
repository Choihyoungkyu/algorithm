N, K = map(int,input().split())
l = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
# s = 0 -> 여 / s = 1 -> 남
for i in range(N):
    s, y = map(int, input().split())
    l[y-1][s] += 1
count = 0
for i in l:
    if i[0] % K == 0:
        count += i[0] // K
    else:
        count += (i[0] // K) + 1
    if i[1] % K == 0:
        count += i[1] // K
    else:
        count += (i[1] // K) + 1
print(count)