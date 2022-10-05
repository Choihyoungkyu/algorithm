lst = []
for _ in range(7):
    n = int(input())
    if n % 2:
        lst.append(n)
if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)