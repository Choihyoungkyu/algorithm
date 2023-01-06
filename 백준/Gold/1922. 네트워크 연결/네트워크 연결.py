import sys
from heapq import heapify, heappop, heappush
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

N = int(input())
M = int(input())
edges = []
for _ in range(M):
    n1, n2, weight = map(int, input().split())
    edges.append([str(n1), str(n2), weight])

def prim(start_node, edges):
    MST = list()
    # 모든 간선의 정보를 adjacent_edges에 저장
    adjacent_egdes = defaultdict(list)
    for n1, n2, weight in edges:
        adjacent_egdes[n1].append((weight, n1, n2))
        adjacent_egdes[n2].append((weight, n2, n1))

    # 연결된 노드 집합에 시작 노드 포함
    connected_nodes = set(start_node)

    # 시작(특정) 노드에 연결된 간선 리스트
    candidate_edge_list = adjacent_egdes[start_node]
    heapify(candidate_edge_list)        # 가중치 순으로 간선 리스트 정렬

    # 최소 가중치를 가지는 간선부터 추출
    while candidate_edge_list:
        # 최소 가중치 간선이 추출됨
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            MST.append((weight, n1, n2))
            # n2의 간선들 중
            # 연결된 노드 집합에 없는 노드의 간선들만
            # 후보 간선 리스트에 추가
            for edge in adjacent_egdes[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    return MST

lst = prim('1', edges)
tot = 0
for i in lst:
    tot += i[0]
print(tot)