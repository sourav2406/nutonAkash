# A recursive python process to print reverse level order

#Basic node for binary tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#compute the height of a binary tree
def _height(node):
    if node is None:
        return 0
    else:
        lheight = _height(node.left)
        rheight = _height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

#print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return 
    if level == 1:
        print(root.data)
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

#print reverse order
def reverseLevelOrder(root):
    h = _height(root)
    for i in reversed(range(1,h+1)):
        printGivenLevel(root,1)

#driver programe
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

reverseLevelOrder(root)