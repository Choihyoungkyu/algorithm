import sys
input = lambda:sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    two_length = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
        continue
    if two_length >= r1 and two_length >= r2:
        if r1 + r2 > two_length:
            print(2)
        elif r1 + r2 < two_length:
            print(0)
        else:
            print(1)
    else:
        r_min = min(r1, r2)
        r_max = max(r1, r2)
        if two_length+r_min < r_max:
            print(0)
        elif two_length+r_min > r_max:
            print(2)
        else:
            print(1)