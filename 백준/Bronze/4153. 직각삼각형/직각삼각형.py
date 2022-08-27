while True:
    lst = list(map(int, input().split()))
    if lst == [0, 0, 0]:
        break
    if lst.pop(lst.index(max(lst)))**2 == lst[0]**2 + lst[1]**2:
        print('right')
    else:
        print('wrong')