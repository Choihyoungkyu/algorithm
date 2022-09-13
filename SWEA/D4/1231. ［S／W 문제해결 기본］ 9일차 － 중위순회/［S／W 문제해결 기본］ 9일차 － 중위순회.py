def inorder(n):
    if n:
        inorder(ch1[n])
        print(st[n], end='')
        inorder(ch2[n])

for idx in range(1, 11):
    K = int(input())
    ch1 = [0] * (K+1)
    ch2 = [0] * (K+1)
    st = [0] * (K+1)
    for i in range(K):
        lst = list(input().split())
        if len(lst) == 4:
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])
            st[int(lst[0])] = lst[1]
        elif len(lst) == 3:
            ch1[int(lst[0])] = int(lst[2])
            st[int(lst[0])] = lst[1]
        elif len(lst) == 2:
            st[int(lst[0])] = lst[1]
    print(f'#{idx}', end=' ')
    inorder(1)
    print()

