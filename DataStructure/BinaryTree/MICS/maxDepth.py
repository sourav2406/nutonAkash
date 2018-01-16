#Max Depth or height of tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxDepth(node):
    if node is None:
        return 0
    else:
        ldepth = maxDepth(node.left)
        rdepth = maxDepth(node.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

#driver programe
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(20)
root.left.right = Node(5)

print("Max depth of tree : {}".format(maxDepth(root)))