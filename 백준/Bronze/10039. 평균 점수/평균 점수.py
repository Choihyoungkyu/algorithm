tot = 0
for _ in range(5):
    a = int(input())
    N = a if a >= 40 else 40
    tot += N
print(int(tot/5))