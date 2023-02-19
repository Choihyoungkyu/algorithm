while True:
    N = int(input())
    if not N:
        break
    tot = 0
    for i in range(1, N+1):
        tot += i
    print(tot)