n = int(input())
lst = map(int, input().split())
cnt = 0
for i in lst:
    if n%10 == i:
        cnt += 1
print(cnt)