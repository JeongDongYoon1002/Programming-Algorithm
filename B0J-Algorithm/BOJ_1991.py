class Node:
    def __init__ (self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(node): # 루트 왼쪽 오른쪽
    print(node.data, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node): # 왼쪽 루트 오른쪽
    
    if node.left != '.':
        inorder(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        inorder(tree[node.right])
 
def postorder(node): # 왼쪽 오른쪽 루트
    
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])

    print(node.data, end='')
n = int(input())
tree = dict()
for _ in range(n):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

preorder(tree['A'])
print()

inorder(tree['A'])
print()

postorder(tree['A'])
print()

