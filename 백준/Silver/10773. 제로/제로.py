N = int(input())

l = []
for i in range(N):
    a = int(input())
    if a != 0:
        l.append(a)
    else:
        l.pop()
print(sum(l))