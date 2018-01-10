from treeNode import Node
from printBinaryTree import printTree

def preOrderPrint(root):
    if root:
        print(root.val,'')
        preOrderPrint(root.left)
        preOrderPrint(root.right)

if __name__ == "__main__":
    ROOT = Node(1)
    ROOT.left = Node(2)
    ROOT.right = Node(3)
    ROOT.left.left = Node(4)
    ROOT.left.right = Node(5)
    ROOT.right.left = Node(6)
    ROOT.right.right = Node(7)

    #printTree(ROOT)
    preOrderPrint(ROOT)

