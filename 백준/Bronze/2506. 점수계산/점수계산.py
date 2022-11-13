
N = int(input())
lst = list(map(int, input().split()))
good = 0
tot = 0
for num in lst:
    if num:
        good += 1
        tot += good
    else:
        good = 0
print(tot)