def solution(n, s, a, b, fares):
    answer = float('INF')
    adjM = [[float('INF')]*n for _ in range(n)]
    for fare in fares:
        adjM[fare[0]-1][fare[1]-1] = fare[2]
        adjM[fare[1]-1][fare[0]-1] = fare[2]
    for i in range(n):
        adjM[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adjM[i][j] = min(adjM[i][j], adjM[i][k] + adjM[k][j])
    for k in range(n):
        answer = min(answer, adjM[s-1][k] + adjM[k][a-1] + adjM[k][b-1])
    return answer