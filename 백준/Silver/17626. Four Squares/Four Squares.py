import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
lst1 = [i*i for i in range(1, int(N**0.5)+1)]
lst2 = []
for i in range(len(lst1)):
    for j in range(i, len(lst1)):
        lst2.append(lst1[i]+lst1[j])
lst2_set = set(lst2)

def answer(N):
    if N in lst1:  # 제곱수면
        return 1
    elif N in lst2:  # 제곱수 두개를 더해서 만들 수 있는 수면
        return 2
    else:
        for square in lst1:  # 제곱 수 중
            if N - square in lst2:  # n에서 제곱수를 뺀 수가 제곱수 두개를 더해서 만들수 있는 수면
                return 3
    return 4

print(answer(N))