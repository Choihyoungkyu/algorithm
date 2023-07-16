N, M = map(int,input().split())
s = ''
for _ in range(N):
    tmp = list(input())
    tmp = tmp[::-1]
    for i in tmp:
        print(i, end='')
    print('')
