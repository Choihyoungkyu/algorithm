M = int(input())
D = int(input())
if M > 2:
    print('After')
elif M < 2:
    print('Before')
else:
    if D > 18:
        print('After')
    elif D < 18:
        print('Before')
    else:
        print('Special')