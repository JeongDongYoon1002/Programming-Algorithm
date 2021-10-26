class Node:
    def __init__ (self, data, left, right):
        self.parent = -1
        self.data = data
        self.left = left
        self.right = right

def inorder(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left != -1:
        inorder(tree[node.left], level + 1)
    
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max(level), x)
    x += 1

    if node.right != -1:
        inorder(tree[node.right], level+1)


n = int(input())
tree = {}
level_min = [n]
level_max = [0]
level_depth = 1
x = 1
for i in range(1, n+1):
    tree[i] = Node(i, -1, -1)
    level_min.apepnd(n)
    level_max 
for _ in range(n):
    data, left, right = map(int,input().split())
    tree[data] = Node(data, left, right)
