import sys

input = lambda: sys.stdin.readline().strip()
N = int(input())

# 1순위 : 별 ( 4 )
# 2순위 : 동 to the 그 to the 라미 ( 3 )
# 3순위 : 네모 ( 2 )
# 4순위 : 세모 ( 1 )
# 무승부 : D
i = 1
while i <= N:
    A = list(map(int, input().split()))
    B = list(map(int,input().split()))
    a = A.pop(0)
    b = B.pop(0)
    if A.count(4) > B.count(4):
        print('A')
    elif A.count(4) < B.count(4):
        print('B')
    else:
        if A.count(3) > B.count(3):
            print('A')
        elif A.count(3) < B.count(3):
            print('B')
        else:
            if A.count(2) > B.count(2):
                print('A')
            elif A.count(2) < B.count(2):
                print('B')
            else:
                if A.count(1) > B.count(1):
                    print('A')
                elif A.count(1) < B.count(1):
                    print('B')
                else:
                    print('D')
    i += 1