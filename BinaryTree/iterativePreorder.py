#python programe to iterative preorder traversal. 

#A binary tree node
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#An iterative process to print preorder traversal
def iterativePreorder(root):

    if root is None:
        return

    nodeStack = []
    nodeStack.append(root)

    while( len(nodeStack) > 0):
        node = nodeStack.pop()
        print(node.data)

        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)

#Driver programe to test above code
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)
iterativePreorder(root)