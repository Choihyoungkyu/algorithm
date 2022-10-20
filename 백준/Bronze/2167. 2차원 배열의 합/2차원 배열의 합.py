import sys
input = lambda:sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    total = 0
    for a in range(i-1, x):
        total += sum(arr[a][j-1:y])
    print(total)