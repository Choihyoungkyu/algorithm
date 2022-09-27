lst = [int(input()) for _ in range(3)]
if sum(lst) == 180:
    if lst[0] == lst[1] and lst[1] == lst[2] and lst[0] == 60:
        print('Equilateral')
    elif lst[0] == lst[1] or lst[1] == lst[2] or lst[0] == lst[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')