N = int(input())
l = list(map(int, input().split()))
l.sort()
k = []
hap = 0
for i in l:
    hap += i
    k.append(hap)
print(sum(k))