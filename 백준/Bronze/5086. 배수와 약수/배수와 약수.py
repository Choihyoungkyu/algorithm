import sys
input = lambda:sys.stdin.readline().strip()

while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    if b % a == 0:
        print('factor')
        continue
    if a % b == 0:
        print('multiple')
        continue
    print('neither')