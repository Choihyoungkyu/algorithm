N = int(input())
n = {3:0, 5:0}

while N > 2:
    if N % 5 == 0:
        n[5] += N // 5
        N -= 5 * (N // 5)
        break
    elif N == 4:
        break
    else:
        if N % 3 == 0:
            N -= 3
            n[3] += 1
        else:
            N -= 5
            n[5] += 1
        
if N == 1 or N == 2 or N == 4:
    print(-1)
else:
    print(n[3] + n[5])