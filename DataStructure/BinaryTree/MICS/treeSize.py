#Tree Size
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sizeTree(node):
    if node is None:
        return 0
    else:
        return (sizeTree(node.left) + 1 + sizeTree(node.right))

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
 
print("Size of the tree is {}".format(sizeTree(root)))