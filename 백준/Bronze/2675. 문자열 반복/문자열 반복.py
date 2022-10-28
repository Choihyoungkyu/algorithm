N = int(input())
for _ in range(N):
    a, s = input().split()
    for i in s:
        print(i*int(a), end='')
    print()