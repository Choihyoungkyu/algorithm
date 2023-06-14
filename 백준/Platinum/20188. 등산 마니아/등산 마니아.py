from collections import deque

N = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int, input().split())
    adjL[i].append(j)
    adjL[j].append(i)

class Node(object):
    def __init__(self, parent, childs, distance):
        self.parent = parent
        self.childs = childs
        self.distance = distance

class Cal(object):
    def __init__(self, node1, node2, Tree):
        self.node1 = node1
        self.node2 = node2
        self.Tree = Tree

    def find_distance(self):
        return Tree[self.node1].distance + Tree[self.node2].distance - Tree[self.find_parent()].distance

    def find_parent(self):
        current1 = self.node1
        current2 = self.node2
        lst = [self.node1, self.node2]
        root = 1
        while True:
            if Tree[current1].parent != 0:
                if Tree[current1].parent in lst: 
                    root = Tree[current1].parent
                    break
                lst.append(Tree[current1].parent)
                current1 = Tree[current1].parent

            if Tree[current2].parent != 0:
                if Tree[current2].parent in lst: 
                    root = Tree[current2].parent
                    break
                lst.append(Tree[current2].parent)
                current2 = Tree[current2].parent

            if Tree[current1].parent == 0 and Tree[current2].parent == 0: 
                root = 1
                break
        return root


Tree = [[] for _ in range(N+1)]
Tree[1] = Node(0, adjL[1], 0)

que = deque()
que.append((1, adjL[1]))

# 트리 만들기
while que:
    parent, lst = que.popleft()
    for i in lst:
        adjL[i].pop(adjL[i].index(parent))
        Tree[i] = Node(parent, adjL[i], Tree[parent].distance+1)
        que.append((i, adjL[i]))

answer = 0
for i in range(1, N):
    for j in range(i+1, N+1):
        tmp = Cal(i, j, Tree)
        answer += tmp.find_distance()
print(answer)