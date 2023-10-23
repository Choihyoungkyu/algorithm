import heapq
def solution(n, works):
    answer = 0
    pque = []
    for work in works:
        heapq.heappush(pque, -work)
        
    while pque and n > 0:
        num = -heapq.heappop(pque)
        if num > 0:
            num -= 1
            n -= 1
            heapq.heappush(pque, -num)
        # print(pque)
    for num in pque:
        answer += num * num
    return answer