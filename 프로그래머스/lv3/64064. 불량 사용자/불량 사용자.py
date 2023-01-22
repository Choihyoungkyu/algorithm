def matching(user, ban):
    for i in range(len(user)):
        if user[i] != ban[i] and ban[i] != "*":
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    visited = [0] * len(user_id)
    res = []
    
    def func(user_id, banned_id, idx):
        if idx == len(banned_id):
            if sum(visited) == len(banned_id) and visited not in res:
                res.append(visited[:])
            return
        for i in range(len(user_id)):
            if not visited[i] and len(user_id[i]) == len(banned_id[idx]) and matching(user_id[i], banned_id[idx]):
                visited[i] = 1
                func(user_id, banned_id, idx+1)
                visited[i] = 0

    func(user_id, banned_id, 0)
    # print(len(res), res)
    return len(res)