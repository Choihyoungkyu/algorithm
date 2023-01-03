from collections import deque

def solution(queue1, queue2):
    answer = -1
    que1 = deque(queue1)
    que2 = deque(queue2)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    cnt = 0
    L = 3*len(queue1)           # que1과 que2의 길이가 같고 양쪽 전부 다 옮길 때까지 반복
                                # que1을 마지막 빼고 전부 que2로 옮긴 다음 다시 que2를 마지막 빼고 전부 que1으로 옮길 경우
                                # que1 -> que2 : l
                                # que2 -> que1 : 2*l
    
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