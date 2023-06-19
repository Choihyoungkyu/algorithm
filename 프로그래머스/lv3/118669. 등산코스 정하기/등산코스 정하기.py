import heapq

def Dijkstra(n, adjL, gates, summits):
    visited = [10000001] * (n+1)
    queue = []
    summit = 0
    minV = float('inf')
    for gate in gates:
        visited[gate] = 0   
        heapq.heappush(queue, [0, gate])
    while queue:
        intensity, node = heapq.heappop(queue)
        if intensity > minV: continue
        for w, i in adjL[node]:
            if not visited[i] or w > minV:  # 출입구인 경우
                continue
            if i in summits and max(intensity, w) < visited[i]:
                visited[i] = max(intensity, w)
                minV = min(minV, visited[i])
                continue
            if max(w, intensity) < visited[i]:
                visited[i] = max(w, intensity)
                heapq.heappush(queue, [max(w, intensity), i])
    lst = []
    for summit in summits:
        lst.append([visited[summit], summit])
    return sorted(lst)[0][::-1]
    

def solution(n, paths, gates, summits):
    answer = []
    adjL = [[] for _ in range(n+1)]
    
    for path in paths:
        i, j, w = path
        adjL[i].append([w, j])
        adjL[j].append([w, i])

    answer = Dijkstra(n, adjL, gates, summits)
        
    return answer