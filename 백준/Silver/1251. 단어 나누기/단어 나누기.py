import sys
input = lambda: sys.stdin.readline().strip()

S = input()
s = list(S)
minV = 150
res = []
idx1 = 0
for i in range(len(s)-3, -1, -1):
    if ord(s[i]) <= minV:
        idx1 = i
        minV = ord(s[i])
        res.append(S[:idx1+1][::-1])
# print(sorted(res)[0])
idx1 = len(sorted(res)[0])-1

minV = 150
idx2 = 0
res = []
for i in range(idx1+1, len(s)-1):
    if ord(s[i]) <= minV:
        idx2 = i
        minV = ord(s[i])
        res.append(S[:idx2+1][::-1])
# print(sorted(res)[0])
idx2 = len(sorted(res)[0])-1

res = ""
res += S[:idx1+1][::-1]
res += S[idx1+1:idx2+1][::-1]
# print(res)
res += S[idx2+1:][::-1]
print(res)