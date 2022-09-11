T = int(input())
for idx in range(1, T+1):
    a, b = map(int, input().split())
    print(f'Case #{idx}: {a} + {b} = {a+b}')