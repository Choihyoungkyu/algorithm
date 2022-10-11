X = int(input())
i = 0
k = 0
while X > k:
    k += i
    i += 1
    re = k - X
if (i-1) % 2 == 0:
    print(f'{i - re - 1}/{re + 1}')
elif (i-1) % 2 == 1:
    print(f'{1 + re}/{i - 1 - re}')