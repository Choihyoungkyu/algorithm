# key를 오른쪽으로 돌리기
def rotate_key(key):
    res = []
    for j in range(len(key)):
        tmp = []
        for i in range(len(key)-1, -1, -1):
            tmp.append(key[i][j])
        res.append(tmp[:])
    return res

# 자물쇠 풀기 시도 
# (자물쇠 해당 위치 == key의 오른쪽 밑) => key의 크기만큼 다 돌림
def unlock(i, j, key, lock):
    key_i, cnt = 0, 0
    for ti in range(i-len(key)+1, i+1):
        key_j = 0
        for tj in range(j-len(key)+1, j+1):
            # 홈을 채우면 카운트 +1
            if 0<=ti<len(lock) and 0<=tj<len(lock) and lock[ti][tj] == 0 and key[key_i][key_j] == 1:
                cnt += 1
            # 홈이 아닌데 key의 홈이 닿으면 ㅈㅈ
            elif 0<=ti<len(lock) and 0<=tj<len(lock) and lock[ti][tj] == 1 and key[key_i][key_j] == 1:
                return 0
            key_j += 1
        key_i += 1
    return cnt

def solution(key, lock):
    answer = False
    zeros = 0
    # 자물쇠의 홈 부분 개수 세기
    for i in range(len(lock)):
        for j in range(len(lock)):
            if not lock[i][j]:
                zeros += 1
    
    # key 모양 4번 * 자물쇠 전체 크기
    for _ in range(4):
        for i in range(len(lock)+len(key)-1):
            for j in range(len(lock)+len(key)-1):
                if zeros == unlock(i, j, key, lock):
                    return True
                
        key = rotate_key(key)
    
    return answer

'''
0 0 0       0 1 0       1 1 0       0 0 1
1 0 0   >   1 0 0   >   0 0 1   >   0 0 1
0 1 1       1 0 0       0 0 0       0 1 0
'''