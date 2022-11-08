import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
length = len(str(N))
tot = (N - 10**(length-1)) * length + length
while length:
    length -= 1
    if length:
        tot += (9*(10**(length-1))*(length))
print(tot)
