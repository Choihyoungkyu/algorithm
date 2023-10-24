# Lv3

def solution(tickets):
    answer = []
    tickets.sort()
    # print(tickets, len(tickets))
    
    visited = [0] * len(tickets)
    flag = False
    
    # "ICN" 시작이 여러 개인 경우 다 돌려야됨
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            idx = i
            visited[idx] = 1
            answer = dfs(tickets, visited, idx, len(tickets)-1, ["ICN"])
            # print(answer)
            if len(answer) == len(tickets)+1:
                return answer
            flag = True
            visited[idx] = 0
        elif flag:
            break
            
    return answer

def dfs(tickets, visited, idx, cnt, plan):
    # print(plan, idx, cnt)
    tmp_plan = plan[:]
    if cnt == 0:
        tmp_plan.append(tickets[idx][1])
        # print(idx, tmp_plan)
        return tmp_plan
    for i in range(len(tickets)):
        if not visited[i] and tickets[idx][1] == tickets[i][0]:
            visited[i] = 1
            tmp_plan = dfs(tickets, visited, i, cnt-1, plan + [tickets[i][0]])
            if len(tmp_plan) == len(tickets) + 1:
                # print(idx, tmp_plan)
                return tmp_plan
            visited[i] = 0
            
    return tmp_plan
    