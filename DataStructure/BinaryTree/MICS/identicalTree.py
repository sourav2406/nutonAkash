#Identical Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def identicalTree(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is not None and node2 is not None:
        return (node1.data == node2.data) and identicalTree(node1.left, node2.left) and identicalTree(node1.right, node2.right)
    return False

#driver programe
root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
 
if identicalTree(root1, root2):
    print("Both trees are identical")
else:
    print("Trees are not identical")