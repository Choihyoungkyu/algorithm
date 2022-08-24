import sys
input = lambda: sys.stdin.readline().strip()

def f(rec1, rec2):
    x1, y1 = rec1[0]
    p1, q1 = rec1[1]
    x2, y2 = rec2[0]
    p2, q2 = rec2[1]

    if (p1 == x2 and y1 == q2) or (p1 == x2 and q1 == y2) :
        return 'c'
    elif p1 < x2 or q1 < y2 or y1 > q2:
        return 'd'
    elif y1 == q2 or p1 == x2 or q1 == y2:
        return 'b'
    else:
        return 'a'
for _ in range(4):
    lst = list(map(int, input().split()))
    rec1 = [lst[:2], lst[2:4]]
    rec2 = [lst[4:6], lst[6:8]]
    if rec1[0][0] > rec2[0][0]:
        rec1, rec2 = rec2, rec1

    print(f(rec1, rec2))