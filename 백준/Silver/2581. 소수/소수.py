M = int(input())
N = int(input())
p = []
if M == 1:
    for i in range(2, N+1):
        for j in range(2, i//2+1):
            if i % j == 0:
                break
            else:
                pass
        else:
            p.append(i)

else:
    for i in range(M, N+1):
        for j in range(2, i//2+1):
            if i % j == 0:
                break
            else:
                pass
        else:
            p.append(i)
if len(p) == 0:
    print(-1)
else:
    print(sum(p))
    print(min(p))