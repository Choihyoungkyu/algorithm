import sys
input = lambda: sys.stdin.readline().strip()
N, K = map(int,input().split())
coin = []
for _ in range(N):
    a = int(input())
    coin.append(a)

count = 0
while K > 0:
    for i in coin[::-1]:
        if K // i >= 1:
            count += K // i
            K = K % i
print(count)