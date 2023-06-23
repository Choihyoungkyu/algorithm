import sys
input = sys.stdin.readline

# N : 접시의 수, d : 초밥의 가짓수, k : 연속해서 먹는 접시의 수, c : 쿠폰 번호
N, d, k, c = map(int, input().split())
sushies = []
for _ in range(N):
    sushies.append(int(input()))
sushies *= 2

s, e = 0, 0
maxLength = 0
lst = []
while s<N or e<N:
    if e-s+1 < k:
        e += 1
    elif e-s+1 == k:
        length = len(set(sushies[s:e+1]))
        if maxLength < length:
            lst = [list(set(sushies[s:e+1]))]
            maxLength = length
        elif maxLength == length:
            lst.append(list(set(sushies[s:e+1])))
        s += 1

answer = len(lst[0])
for i in lst:
    if c not in i:
        answer += 1
        break
print(answer)