lst = list(map(int, input().split()))
check = lst[0] - lst[1]
for i in range(1, len(lst)-1):
    if check != lst[i] - lst[i+1]:
        print('mixed')
        break
else:
    if check == -1:
        print('ascending')
    else:
        print('descending')