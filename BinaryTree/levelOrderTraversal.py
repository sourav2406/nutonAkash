from treeNode import Node
from printBinaryTree import printTree

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

def printLevelOrder(tree):
    h = height(tree)
    print('\n')
    for i in range(1, h+1):
        printGivenLevel(tree, i)

def printGivenLevel(tree,level):
    if tree is None:
        return 0
    if level == 1:
        print(tree.val, end='')
    elif level > 1:
        printGivenLevel(tree.left, level-1)
        printGivenLevel(tree.right, level-1)


ROOT = Node(1)
ROOT.left = Node(2)
ROOT.right = Node(3)
ROOT.left.left = Node(4)
ROOT.left.right = Node(5)
ROOT.right.left = Node(6)
ROOT.right.right = Node(7)

printTree(ROOT)

printLevelOrder(ROOT)
