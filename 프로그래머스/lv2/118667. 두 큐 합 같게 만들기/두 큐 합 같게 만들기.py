from collections import deque

def solution(queue1, queue2):
    answer = -1
    que1 = deque(queue1)
    que2 = deque(queue2)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    cnt = 0
    L = 3*len(queue1)
    
    while cnt < L:
        if tot1 == tot2:
            answer = cnt
            break
        cnt += 1
        if tot1 > tot2:
            tmp = que1.popleft()
            que2.append(tmp)
            tot1 -= tmp
            tot2 += tmp
        else:
            tmp = que2.popleft()
            que1.append(tmp)
            tot1 += tmp
            tot2 -= tmp
    
    return answer