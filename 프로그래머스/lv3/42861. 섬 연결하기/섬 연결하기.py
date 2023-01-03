# Lv3
def solution(n, costs):
    answer = 0
    adjM = [[0]*(n+1) for _ in range(n+1)]
    for cost in costs:
        adjM[cost[0]][cost[1]] = cost[2]
        adjM[cost[1]][cost[0]] = cost[2]
    
    for i in adjM:
        print(*i)

    def prim(r, V):
        MST = [0] * (V)
        MST[r] = 1
        s = 0
        for _ in range(V-1):
            u = 0
            minV = float('inf')
            for i in range(V):
                if MST[i] == 1:
                    for j in range(V):
                        if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                            u = j
                            minV = adjM[i][j]
            s += minV
            MST[u] = 1
        return s
    answer = prim(0, n)
                
    return answer