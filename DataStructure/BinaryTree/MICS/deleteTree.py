#delete an binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def delTree(root):
    if root is None:
        return None

    delTree(root.left)
    delTree(root.right)
    print("deleting Node : {}".format(root.data))
    del root

#dirver function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right= Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.left.right = Node(8)

delTree(root)
