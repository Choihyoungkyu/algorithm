N = int(input())
Numbers = list(map(int, input().split()))
Numbers.sort()

answer = 0

def Two_Pointer(idx, target):
    s, e = 0, N-1
    if s == idx: s += 1
    if e == idx: e -= 1
    while s < e:
        tot = Numbers[s] + Numbers[e]
        if tot == target:
            return 1
        elif tot < target:
            s += 1
            if s == idx: s += 1
        else:
            e -= 1
            if e == idx: e -= 1
    return 0

for i in range(N):
    answer += Two_Pointer(i, Numbers[i])

print(answer)