import sys
sys.setrecursionlimit(10**6)

# data = [value, x, y]
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
class BinaryTree(list):
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data[0] < node.data[0]:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
    def pre_order_traversal(self):
        res = []
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                if root is not None:
                    res.append(root.data[2])
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
                return res
        return _pre_order_traversal(self.root)
    
    def post_order_traversal(self):
        res = []
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                if root is not None:
                    res.append(root.data[2])
                return res
        return _post_order_traversal(self.root)

                

def solution(nodeinfo):
    answer = []
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key = lambda x : x[1], reverse=True)
    
    tree = BinaryTree()
    for node in nodeinfo:
        tree.insert(node)
        
    answer.append(tree.pre_order_traversal())
    answer.append(tree.post_order_traversal())
    
    return answer