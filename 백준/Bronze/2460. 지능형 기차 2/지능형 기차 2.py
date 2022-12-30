tot = 0
maxV = 0
for i in range(10):
    a, b = map(int, input().split())
    tot += b-a
    maxV = max(tot, maxV)
print(maxV)