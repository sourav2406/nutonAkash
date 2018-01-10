#simple binary tree
from treeNode import Node

if __name__ == "__main__":
    ROOT = Node(1)
    ROOT.left = Node(2)
    ROOT.right = Node(3)

    print(ROOT.val)
    print(ROOT.left.val)
    print(ROOT.right.val)
