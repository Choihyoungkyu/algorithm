import sys
input = lambda:sys.stdin.readline().strip()

lst1 = []
lst2 = []
for _ in range(4):
    lst1.append(int(input()))
for _ in range(2):
    lst2.append(int(input()))
lst1.sort()
lst2.sort()
tot = sum(lst1[1:])
tot += lst2[1]
print(tot)