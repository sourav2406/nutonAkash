"""New binary tree Node"""
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

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

def printTree(root):
    if root:
        print(root.val, end='')
        printTree(root.left)
        printTree(root.right)
