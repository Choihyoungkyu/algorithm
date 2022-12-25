
tot = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    tot += b%a
print(tot)