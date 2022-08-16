import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
switch = list(map(int, input().split()))

for _ in range(int(input())):
    a, b = map(int, input().split())

    # 남자일 경우
    if a == 1:                                          
        for i in range(b-1, N, b):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
    
    # 여자일 경우
    else:
        maxV = 0
        if b <= (N // 2):
            for k in range(b):
                if switch[b-1-k] == switch[b-1+k]:
                    maxV = k
                else:
                    break
            for j in range(b-1-maxV, b+maxV):
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1

        else:
            for k in range(N - b + 1):
                if switch[b-1-k] == switch[b-1+k]:
                    maxV = k
                else:
                    break
            for j in range(b-1-maxV, b+maxV):
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1

# 출력
for i in range(N):
    print(switch[i], end=' ')
    if (i+1) % 20 == 0 and i != 0:
        print()