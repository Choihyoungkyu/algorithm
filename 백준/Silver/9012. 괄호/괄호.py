N = int(input())
k = 1
while k <= N:
    count = 0
    s = input()
    for i in s:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            print('NO')
            break
    else:
        if count == 0:
            print('YES')
        else:
            print('NO')
    k += 1