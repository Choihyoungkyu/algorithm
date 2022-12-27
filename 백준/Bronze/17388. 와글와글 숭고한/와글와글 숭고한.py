import sys
input = lambda:sys.stdin.readline().strip()

S, K, H = map(int, input().split())
if S+K+H >= 100:
    print('OK')
else:
    minV = min(S, K, H)
    if S == minV:
        print('Soongsil')
    elif K == minV:
        print('Korea')
    else:
        print('Hanyang')