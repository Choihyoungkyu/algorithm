import sys, heapq
input = sys.stdin.readline

queue = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x < 0:
        heapq.heappush(queue, (-x, x))
    elif x > 0:
        heapq.heappush(queue, (x, x))
    else:
        try:
            print(heapq.heappop(queue)[1])
        except:
            print(0)