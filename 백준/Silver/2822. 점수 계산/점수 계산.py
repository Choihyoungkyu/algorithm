l = []
for i in range(8):
    l.append(int(input()))
k = [0]
for i in l:
    k.append(i)
    if len(k) > 5:
        k.pop(k.index(min(k)))
o = []
for i in range(5):
    p = l.index(k[i]) + 1
    o.append(p)
print(sum(k))
for i in o:
    print(i, end=' ')