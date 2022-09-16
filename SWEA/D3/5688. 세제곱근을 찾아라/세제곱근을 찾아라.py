T = int(input())
for idx in range(1, T+1):
    N = int(input())
    DP = [0] * (int(N**(1/3))+2)
    i = int(N**(1/3))-1
    flag = False
    while i <= int(N**(1/3))+1:
        DP[i] = i ** 3
        if DP[i] == N:
            print(f'#{idx} {i}')
            flag = True
            break
        i += 1
    if not flag:
        print(f'#{idx} -1')
