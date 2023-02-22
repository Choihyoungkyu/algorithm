def rotate_key(key):
    res = []
    for j in range(len(key)):
        tmp = []
        for i in range(len(key)-1, -1, -1):
            tmp.append(key[i][j])
        res.append(tmp[:])
    return res

def unlock(i, j, key, lock):
    key_i, cnt = 0, 0
    for ti in range(i-len(key)+1, i+1):
        key_j = 0
        for tj in range(j-len(key)+1, j+1):
            if 0<=ti<len(lock) and 0<=tj<len(lock) and lock[ti][tj] == 0 and key[key_i][key_j] == 1:
                cnt += 1
            elif 0<=ti<len(lock) and 0<=tj<len(lock) and lock[ti][tj] == 1 and key[key_i][key_j] == 1:
                return 0
            key_j += 1
        key_i += 1
    return cnt

def solution(key, lock):
    answer = False
    zeros = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            if not lock[i][j]:
                zeros += 1
            
    cnt = 0
    for _ in range(4):
        for i in range(len(lock)+len(key)-1):
            for j in range(len(lock)+len(key)-1):
                cnt += 1
                if zeros == unlock(i, j, key, lock):
                    # print(cnt, i, j, key)
                    return True
                
        
        key = rotate_key(key)
    
    return answer

'''
0 0 0       0 1 0       1 1 0       0 0 1
1 0 0   >   1 0 0   >   0 0 1   >   0 0 1
0 1 1       1 0 0       0 0 0       0 1 0
'''