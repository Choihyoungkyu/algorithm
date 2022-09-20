a, b, c, d = map(int, input().split())
tot = a+b+c+d
x, y, z, m = map(int, input().split())
tot2 = x+y+z+m
print(tot) if tot>=tot2 else print(tot2)