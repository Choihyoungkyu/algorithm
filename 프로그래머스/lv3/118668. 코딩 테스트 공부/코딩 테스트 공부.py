def solution(alp, cop, problems):
    max_req, max_cop = alp, cop
    for problem in problems:
        max_req = max(max_req, problem[0])
        max_cop = max(max_cop, problem[1])
    print(max_req, max_cop)
    DP = [[float('INF')] * (max_cop+1) for _ in range(max_req+1)]
    DP[alp][cop] = 0
    for i in range(alp, max_req+1):
        for j in range(cop, max_cop+1):
            if i < max_req:
                DP[i+1][j] = min(DP[i+1][j], DP[i][j] + 1)
            if j < max_cop:
                DP[i][j+1] = min(DP[i][j+1], DP[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i+alp_rwd, max_req)
                    new_cop = min(j+cop_rwd, max_cop)
                    DP[new_alp][new_cop] = min(DP[new_alp][new_cop], DP[i][j] + cost)

    return DP[max_req][max_cop]