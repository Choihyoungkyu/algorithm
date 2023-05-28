import sys
input = lambda:sys.stdin.readline().strip()

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2

    while p and heap[c] > heap[p]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq():
    global last
    if last == 0:
        return 0
    else:
        tmp = heap[1]
        heap[1] = heap[last]
        last -= 1
        p = 1
        c = 2 * p
        while c <= last:
            if c+1 <= last and heap[c] < heap[c+1]:
                c += 1
            if heap[p] < heap[c]:
                heap[p], heap[c] = heap[c], heap[p]
                p = c
                c = p * 2
            else:
                break
        return tmp

E = int(input())
heap = [0] * (E+1)
last = 0
for _ in range(E):
    n = int(input())
    if n == 0:
        print(deq())
    else:
        enq(n)