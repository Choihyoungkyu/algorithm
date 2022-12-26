n = int(input())
if ((n-1) // 4) % 2 == 0:
    print((n-1)%4+1)
else:
    print(5-(n-1)%4)