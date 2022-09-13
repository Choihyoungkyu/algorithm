# 전위순회
def preorder(n):
    if n != '.':
        print(n, end='')        # visit(n)
        preorder(dic1[n])
        preorder(dic2[n])

# 중위순회
def inorder(n):
    if n != '.':
        inorder(dic1[n])
        print(n, end='')        # visit(n)
        inorder(dic2[n])

# 후위순회
def postorder(n):
    if n != '.':
        postorder(dic1[n])
        postorder(dic2[n])
        print(n, end='')        # visit(n)

N = int(input())
dic1 = {}
dic2 = {}
ch1 = [0]*(N + 1)
ch2 = [0]*(N + 1)
for i in range(1, N+1):
    x, y, z = input().split()
    dic1[x] = y
    dic2[x] = z

root = 'A'

# 전위순회
preorder(root)
print()

# 중위순회
inorder(root)
print()


# 후위순회
postorder(root)
